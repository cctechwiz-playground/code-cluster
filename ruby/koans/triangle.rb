# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   :equilateral  if all sides are equal
#   :isosceles    if exactly 2 sides are equal
#   :scalene      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.rb
# and
#   about_triangle_project_2.rb
#
def validate(*args)
    a, b, c = *(args.sort)
    raise TriangleError, "zero side" if((a == 0) || (b == 0) || (c == 0))
    raise TriangleError, "negative side" if((a < 0) || (b < 0) || (c < 0))
    raise TriangleError, "invalid sides" if((a + b) < c || (a + b) == c)
end

def triangle(a, b, c)
    begin
        validate(a, b, c)
    rescue TriangleError => ex
        raise ex 
    end

    return :equilateral if a == b && a == c && b == c
    return :isosceles if a == b || a == c || b == c
    return :scalene
end

# Error class used in part 2.  No need to change this code.
class TriangleError < StandardError
end
