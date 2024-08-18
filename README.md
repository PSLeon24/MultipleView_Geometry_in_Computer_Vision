# MultipleView_Geometry_in_Computer_Vision
# Concepts
## 1. Planar Geometry
- 2차원 사원평면
  - 1) 점과 선
    - (1) 선의 동차 표현(Homogeneous Representation of Lines)
      - l = (a, b, c)ᵀ
    - (2) 점의 동차 표현(Homogeneous Representation of Points)
      - x = (x, y, 1)ᵀ
    - (3) 자유도(Degrees of Freedom)
      - 이미지가 변환(transformation)될 때 최소한으로 필요로 하는 독립변수의 수
    - (4) 선의 교점
      - x = l X l' (외적(cross product)을 사용해서 구할 수 있음)
    - (5) 점을 연결하는 직선
      - l = x X x' (외적(cross product)을 사용해서 구할 수 있음) 
  - 2) 이상점과 무한선
  - 3) 사영변환

# Important Results
- (1) 점 x가 직선 l상에 있을 필요충분조건 xᵀl = lᵀx = x·l = 0
- (2) 두 직선 l과 l'의 교점 x = l X l' (X: cross product)
- (3) 두 점 x와 x'을 지나는 직선은 l = x X x' (X: cross product)
