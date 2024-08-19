# MultipleView_Geometry_in_Computer_Vision
# Concepts
## 1. Planar Geometry
- a. 점과 선
  - (1) 선의 동차 표현(Homogeneous Representation of Lines)
    - l = (a, b, c)ᵀ
  - (2) 점의 동차 표현(Homogeneous Representation of Points)
    - x = (x, y, 1)ᵀ
  - (3) 자유도(Degrees of Freedom)
    - 이미지가 변환(transformation)될 때 최소한으로 필요로 하는 독립변수의 수
  - (4) 선의 교점
    - x = l X l' (외적(cross product)을 사용해서 구할 수 있음)
    - ![image](https://github.com/user-attachments/assets/53e90da2-9f64-46f0-a941-e994e7348c41)

  - (5) 점을 연결하는 직선
    - l = x X x' (외적(cross product)을 사용해서 구할 수 있음)

---

- b. 이상점과 무한선
  - ![스크린샷, 2024-08-19 10-32-06](https://github.com/user-attachments/assets/eb184a53-1c74-40e9-abb2-5f784854dac2)
  - ![image](https://github.com/user-attachments/assets/c451185c-bdb8-4d09-bbcb-f6ed45699c5a)

  - 평행선의 교점
    - l X l' = (c' - c)(b, -a, 0)ᵀ (외적(cross product)을 사용해서 구할 수 있음)
  - (1) 이상점(ideal point): x3 = 0인 점
    - x = (x1, x2, 0)ᵀ
  - (2) 무한선(line at infinity): 평면에서 직선 방향의 집합
    - l∞ = (0, 0, 1)ᵀ
  - (3) 사영평면의 모델
    - 기하학적으로 봤을 때, 2차원 사영공간(P^2)운 3차원 공간(R^3)에서 원점을 지나는 모든 직선들의 집합
    - R^3 공간 상의 원점을 지나는 직선과 x3 = 1인 평면이 교차하는 점이 곧 P^2 공간 상의 한 점이 됨
    - ![image](https://github.com/user-attachments/assets/598f8b2a-46d1-4838-858f-11c67c0c3157)

  - (4) 쌍대성(duality)
    - 2차원 사영공간(P^2)에서는 점과 직선이 쌍대성 혹은 대칭성(duality)을 가짐
      - i.e., 직선 l 위의 한 점 x는 xᵀl=0 또는 lᵀx=0과 같이 두 가지 방법으로 표현할 수 있음
    - 즉, 두 점을 통과하는 직선의 공식은 두 직선이 교차하는 한 점의 공식과 대칭임
 
---

  - c. 사영변환

# Important Results
- (1) 점 x가 직선 l상에 있을 필요충분조건 xᵀl = lᵀx = x·l = 0
- (2) 두 직선 l과 l'의 교점 x = l X l' (X: cross product)
- (3) 두 점 x와 x'을 지나는 직선은 l = x X x' (X: cross product)
- (4) 쌍대성의 원칙: 2차원 사영기하학의 모든 정리는 점과 선의 역할을 교환한 쌍대 정리가 있음

## References
[1] https://www.r-5.org/files/books/computers/algo-list/image-processing/vision/Richard_Hartley_Andrew_Zisserman-Multiple_View_Geometry_in_Computer_Vision-EN.pdf
[2] https://alida.tistory.com/13
