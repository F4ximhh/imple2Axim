from turtle import*
color('red','pink')
begin_fill()
while True:
  forward(45)
  left(100)
  if abs(pos()) < 1:
    break
end_fill() 
color('red','blue')
begin_fill()
while True:
  forward(600)
  right(570)
  if abs(pos()) < 1:
    break
done()
