# MultipleView_Geometry_in_Computer_Vision
# Concepts
## 1. Planar Geometry
- a. Points and lines
  - (1) Homogeneous Representation of Lines
    - l = (a, b, c)ᵀ
  - (2) Homogeneous Representation of Points
    - x = (x, y, 1)ᵀ
  - (3) Degrees of Freedom
    - The minimum number of independent variables required when an image undergoes a transformation
  - (4) Intersection of lines
    - x = l X l' (can be obtained using the cross product)
    - ![image](https://github.com/user-attachments/assets/53e90da2-9f64-46f0-a941-e994e7348c41)

  - (5) The line joining two points
    - l = x X x' (can be obtained using the cross product)

---

- b. Ideal points and the line at infinity
  - ![screenshot, 2024-08-19 10-32-06](https://github.com/user-attachments/assets/eb184a53-1c74-40e9-abb2-5f784854dac2)
  - ![image](https://github.com/user-attachments/assets/c451185c-bdb8-4d09-bbcb-f6ed45699c5a)

  - Intersection of parallel lines
    - l X l' = (c' - c)(b, -a, 0)ᵀ (can be obtained using the cross product)
  - (1) Ideal point: a point with x3 = 0
    - x = (x1, x2, 0)ᵀ
  - (2) Line at infinity: the set of line directions in the plane
    - l∞ = (0, 0, 1)ᵀ
  - (3) A model of the projective plane
    - Geometrically, the two-dimensional projective space (P^2) is the set of all lines passing through the origin in three-dimensional space (R^3)
    - The point where a line through the origin in R^3 space intersects the plane x3 = 1 is precisely a point in P^2 space
    - ![image](https://github.com/user-attachments/assets/598f8b2a-46d1-4838-858f-11c67c0c3157)

  - (4) Duality
    - In two-dimensional projective space (P^2), points and lines possess duality (or symmetry)
      - i.e., a point x on a line l can be expressed in two ways, as xᵀl=0 or as lᵀx=0
    - That is, the formula for the line passing through two points is symmetric with the formula for the point at which two lines intersect

---

  - c. Projective transformation

# Important Results
- (1) The necessary and sufficient condition for a point x to lie on a line l is xᵀl = lᵀx = x·l = 0
- (2) The intersection x of two lines l and l' is x = l X l' (X: cross product)
- (3) The line passing through two points x and x' is l = x X x' (X: cross product)
- (4) The principle of duality: every theorem of two-dimensional projective geometry has a dual theorem obtained by exchanging the roles of points and lines

## References
[1] https://www.r-5.org/files/books/computers/algo-list/image-processing/vision/Richard_Hartley_Andrew_Zisserman-Multiple_View_Geometry_in_Computer_Vision-EN.pdf
[2] https://alida.tistory.com/13
