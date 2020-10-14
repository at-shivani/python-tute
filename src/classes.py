

 # math_func()
def gcd(a, b):
	if a == 0 or b == 0:
		return a if a != 0 else b

	return gcd(b%a, a)


class Fraction:
	def __init__(self, num=0, den=1):
		self.n = num
		self.d = den
		self.simplify()
		self.isPos = self.n * self.d > 0
		if self.isPos:
			self.n = abs(self.n)
			self.d = abs(self.d)
		else:
			self.n = -abs(self.n)
			self.d = abs(self.d)

	def simplify(self): 
		g = gcd(self.n, self.d)
		self.n //= g
		self.d //= g


	def __add__(self, frc):
		n1, n2, d1, d2 = self.n, frc.n, self.d, frc.d
		mult = d1 * d2
		sum_ = d1*n2 + n1*d2
		ans = Fraction(sum_, mult)
		# ans.simplify()

		return ans

	def __sub__(self, frc):
		frc.n *= -1
		return self + frc


	def __str__(self):
		return f'{self.n}/{self.d}'




# one_fifth = Fraction(1, 5)
# # print(one_fifth)
# f1 = Fraction(7,8)
# f2 = Fraction(11,12)
# ans = f1 - f2
# # ans = Fraction(5, 10)
# print(ans)

