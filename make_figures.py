# -*- coding: utf-8 -*-
"""Figures for the multiple view geometry notes.

Every panel is produced by applying the matrix it is about. The transformation
hierarchy is four real homographies applied to one shape, the vanishing point is
where the transformed parallel lines actually meet, and the RANSAC panel is a
real estimation run with real outliers. A figure drawn to look plausible would
hide exactly the cases these notes are trying to make visible.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

OUT = "figures"
BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#999999"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.dpi": 150})


def apply_h(H, pts):
    """Homogeneous transform, then divide through by the third coordinate."""
    p = np.vstack([pts, np.ones(pts.shape[1])])
    q = H @ p
    return q[:2] / q[2]


def fig_hierarchy():
    """What each rung of the hierarchy keeps, shown on one shape."""
    sq = np.array([[0, 1, 1, 0, 0, 0.5],
                   [0, 0, 1, 1, 0, 1.4]])          # square plus a roof marker
    th = np.deg2rad(20)
    R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    mats = [
        ("Euclidean\n3 dof", np.block([[R, np.array([[0.2], [0.1]])],
                                       [np.zeros((1, 2)), np.ones((1, 1))]]),
         "lengths, angles"),
        ("Similarity\n4 dof", np.block([[1.4 * R, np.array([[0.2], [0.1]])],
                                        [np.zeros((1, 2)), np.ones((1, 1))]]),
         "angles, length ratios"),
        ("Affine\n6 dof", np.array([[1.2, 0.5, 0.1],
                                    [0.1, 0.9, 0.1],
                                    [0.0, 0.0, 1.0]]),
         "parallelism, area ratios"),
        ("Projective\n8 dof", np.array([[1.1, 0.35, 0.1],
                                        [0.15, 0.95, 0.1],
                                        [0.30, 0.22, 1.0]]),
         "collinearity, cross ratio"),
    ]
    fig, axes = plt.subplots(1, 4, figsize=(11.4, 3.2))
    for ax, (name, H, keeps) in zip(axes, mats):
        out = apply_h(H, sq)
        ax.plot(sq[0], sq[1], color=GREY, lw=1.2, ls=":", label="original")
        ax.plot(out[0], out[1], color=BLUE, lw=2, label="transformed")
        ax.set_title("%s\ninvariant: %s" % (name, keeps), fontsize=9)
        ax.set_aspect("equal")
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlim(-0.6, 2.6); ax.set_ylim(-0.6, 2.6)
    axes[0].legend(frameon=False, fontsize=8, loc="upper left")
    fig.suptitle("Each rung adds degrees of freedom and gives up an invariant "
                 "(H&Z §2.4)", fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.88))
    fig.savefig(os.path.join(OUT, "hierarchy.png"))
    plt.close(fig)


def fig_vanishing():
    """Parallel lines meet at an ideal point; a projectivity brings it into view."""
    H = np.array([[1.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.28, 0.0, 1.0]])
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.4, 3.6))
    ys = np.linspace(-1.5, 1.5, 7)
    xs = np.linspace(0, 6, 200)
    for y in ys:
        line = np.stack([xs, np.full_like(xs, y)])
        a1.plot(line[0], line[1], color=BLUE, lw=1.2)
        out = apply_h(H, line)
        a2.plot(out[0], out[1], color=BLUE, lw=1.2)
    a1.set_title("World: parallel lines, meeting only at the ideal point\n"
                 "$x_\\infty = (1,0,0)^\\top$", fontsize=9)
    # the image of the ideal point is where the transformed lines converge
    v = H @ np.array([1.0, 0.0, 0.0])
    v = v[:2] / v[2]
    a2.plot(*v, "o", color=ORANGE, ms=9, mfc="none", mew=2)
    a2.annotate("vanishing point\n$H x_\\infty$ = (%.2f, %.2f)" % (v[0], v[1]),
                xy=v, xytext=(v[0] - 2.4, v[1] + 1.1), fontsize=8, color=ORANGE,
                arrowprops=dict(arrowstyle="->", color=ORANGE))
    a2.set_title("Image: the projectivity maps $l_\\infty$ to a finite line,\n"
                 "so parallels visibly converge", fontsize=9)
    for ax in (a1, a2):
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlim(-0.4, 6.4); ax.set_ylim(-2.6, 2.6)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "vanishing.png"))
    plt.close(fig)


def fig_epipolar():
    """Real F from two real projection matrices, and the lines it produces."""
    K = np.array([[800.0, 0, 320], [0, 800.0, 240], [0, 0, 1]])
    th = np.deg2rad(-12)
    R = np.array([[np.cos(th), 0, np.sin(th)], [0, 1, 0], [-np.sin(th), 0, np.cos(th)]])
    t = np.array([[1.2], [0.0], [0.1]])
    rng = np.random.default_rng(3)
    X = np.vstack([rng.uniform(-1, 1, 12), rng.uniform(-0.8, 0.8, 12),
                   rng.uniform(4, 7, 12)])

    def proj(P, X):
        x = P @ np.vstack([X, np.ones(X.shape[1])])
        return x[:2] / x[2]

    P1 = K @ np.hstack([np.eye(3), np.zeros((3, 1))])
    P2 = K @ np.hstack([R, t])
    x1, x2 = proj(P1, X), proj(P2, X)
    # F = [e']_x P' P^+  reduces to K^-T [t]_x R K^-1 for this pair
    tx = np.array([[0, -t[2, 0], t[1, 0]], [t[2, 0], 0, -t[0, 0]], [-t[1, 0], t[0, 0], 0]])
    F = np.linalg.inv(K).T @ tx @ R @ np.linalg.inv(K)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.0, 3.9))
    a1.scatter(x1[0], x1[1], s=22, color=BLUE)
    a1.set_title("View 1: points $x$", fontsize=9)
    a2.scatter(x2[0], x2[1], s=22, color=BLUE, zorder=3)
    xs = np.array([0, 640])
    for i in range(X.shape[1]):
        l = F @ np.array([x1[0, i], x1[1, i], 1.0])       # epipolar line l' = F x
        ys = -(l[0] * xs + l[2]) / l[1]
        a2.plot(xs, ys, color=ORANGE, lw=0.9, alpha=0.8)
    resid = np.abs([np.array([x2[0, i], x2[1, i], 1.0]) @ F @ np.array([x1[0, i], x1[1, i], 1.0])
                    for i in range(X.shape[1])]).max()
    a2.set_title("View 2: every $x'$ lies on its line $l' = Fx$\n"
                 "max $|x'^\\top F x|$ = %.1e" % resid, fontsize=9)
    for ax in (a1, a2):
        ax.set_xlim(0, 640); ax.set_ylim(480, 0)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_aspect("equal")
    fig.suptitle("Epipolar geometry: a point in one view constrains its match to a line, "
                 "not a point (H&Z ch. 9)", fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig(os.path.join(OUT, "epipolar.png"))
    plt.close(fig)


def fig_ransac():
    """DLT alone versus DLT inside RANSAC, on the same contaminated matches."""
    rng = np.random.default_rng(7)
    H_true = np.array([[1.05, 0.18, 12.0], [-0.12, 0.98, 8.0], [0.0004, 0.0002, 1.0]])
    n_in, n_out = 60, 26
    p = np.vstack([rng.uniform(0, 400, n_in), rng.uniform(0, 300, n_in)])
    q = apply_h(H_true, p) + rng.normal(0, 1.0, (2, n_in))
    p_out = np.vstack([rng.uniform(0, 400, n_out), rng.uniform(0, 300, n_out)])
    q_out = np.vstack([rng.uniform(0, 400, n_out), rng.uniform(0, 300, n_out)])
    P = np.hstack([p, p_out])
    Q = np.hstack([q, q_out])

    def dlt(p, q):
        A = []
        for i in range(p.shape[1]):
            x, y = p[0, i], p[1, i]
            u, v = q[0, i], q[1, i]
            A.append([-x, -y, -1, 0, 0, 0, u * x, u * y, u])
            A.append([0, 0, 0, -x, -y, -1, v * x, v * y, v])
        _, _, Vt = np.linalg.svd(np.array(A))
        return Vt[-1].reshape(3, 3)

    H_all = dlt(P, Q)
    best, best_n = None, -1
    for _ in range(600):
        idx = rng.choice(P.shape[1], 4, replace=False)
        try:
            H = dlt(P[:, idx], Q[:, idx])
            e = np.linalg.norm(apply_h(H, P) - Q, axis=0)
        except np.linalg.LinAlgError:
            continue
        k = int((e < 3.0).sum())
        if k > best_n:
            best, best_n = H, k
    inl = np.linalg.norm(apply_h(best, P) - Q, axis=0) < 3.0
    H_ran = dlt(P[:, inl], Q[:, inl])

    e_all = np.linalg.norm(apply_h(H_all, P[:, :n_in]) - Q[:, :n_in], axis=0)
    e_ran = np.linalg.norm(apply_h(H_ran, P[:, :n_in]) - Q[:, :n_in], axis=0)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.6))
    a1.scatter(P[0, :n_in], P[1, :n_in], s=14, color=BLUE, label="true matches")
    a1.scatter(P[0, n_in:], P[1, n_in:], s=22, color=ORANGE, marker="x",
               label="outliers (%d of %d)" % (n_out, P.shape[1]))
    a1.set_title("Correspondences given to the estimator", fontsize=9)
    a1.legend(frameon=False, fontsize=8)
    a1.set_xticks([]); a1.set_yticks([])
    bins = np.linspace(0, 60, 45)
    a2.hist(e_all, bins=bins, color=ORANGE, alpha=0.75,
            label="DLT on all points   median %.1f px" % np.median(e_all))
    a2.hist(e_ran, bins=bins, color=BLUE, alpha=0.8,
            label="DLT inside RANSAC   median %.1f px" % np.median(e_ran))
    a2.set_xlabel("reprojection error on the true matches (px)")
    a2.set_ylabel("count")
    a2.set_title("Least squares has no defence against 30%% outliers\n"
                 "(RANSAC recovered %d of %d inliers)" % (int(inl[:n_in].sum()), n_in),
                 fontsize=9)
    a2.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "ransac.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    fig_hierarchy()
    fig_vanishing()
    fig_epipolar()
    fig_ransac()
    print("wrote", sorted(os.listdir(OUT)))
