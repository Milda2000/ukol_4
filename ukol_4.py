import line_snapper

#coordinates =[[ -742188.6592558697, -1059396.3564614803 ],[ -742185.1865536831, -1059399.8291636668 ],[ -742171.9574453533, -1059422.6494780332 ],[ -742151.782932654, -1059454.3995980248 ],[ -742145.8297289051, -1059459.6913013533 ],[ -742138.5537243225, -1059464.65220448 ],[ -742129.2932184935, -1059467.298106145 ],[ -742118.7099118307, -1059468.6210069768 ],[ -742099.527499754, -1059466.305905521 ],[ -742078.3607864268, -1059461.0142021887 ],[ -742045.2878656052, -1059452.7459969819 ],[ -742027.0976541527, -1059449.7693951093 ],[ -742013.2071454078, -1059449.7693951093 ],[ -741998.6080362163, -1059450.7690957375 ]]

#testovani
delka = 8
p1 = line_snapper.Point(0,0)
p2 = line_snapper.Point(20,0)
print(p1)
seg = line_snapper.Segment(p1,p2)
print(seg)
line = line_snapper.Polyline(seg)
new_line = line.divide_long_segments(delka)
new_points = new_line.points()
print(new_points)
print(new_points[1][0])