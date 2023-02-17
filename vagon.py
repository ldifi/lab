mesto = input()
mesto = int(mesto)
if mesto > 0:
  if mesto // 2 == 1:
     if 1 >= mesto <= 36:
        print("Купе, верхняя полка")
     elif 37 >= mesto <= 54:
        print("Боковая койка, верхняя полка")
  else:
     if 1 >= mesto <= 36:
         print("Купе, нижняя полка")
     elif 37 >= mesto <= 54:
        print("Боковая койка, нижняя полка")
