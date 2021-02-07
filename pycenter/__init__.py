import fire

class Pycenter(object):
  """A simple calculator class."""

  def pctof(self, percent, number):
      result = ((percent / 100) * number)
      if float(result).is_integer():
        return ("%d%% of %d is: %d" % (percent, number, int(result)))
      else:
        return ("%f%% of %f is: %f" % (percent, number, float(result)))

  def pctadd(self, percent, number):
    add = (percent * number) / 100
    result = (add + number)
    if float(result).is_integer():
      return ("%d%% to %d is: %d" % (percent, number, int(result)))
    else:
      return ("%f%% to %f is: %f" % (percent, number, float(result)))
  
  def pctmore(self, num1, num2):
    add = ((num1 - num2) / num2)
    result = add * 100
    if num1 < num2:
        return (f'{num1:.2f} is less than {num2:.2f} use "pctless" instead')
    if float(result).is_integer():
        return (f'{num1:.2f} is {result:.2f}% bigger than {num2:.2f}')
    else:
      return (f'{num1:.2f} is {result:.2f}% bigger than {num2:.2f}')

  def pctless(self, num1, num2):
    subtract = ((num1 - num2) / num1)
    result = subtract * 100
    if num1 > num2:
      return (f'{num1:.2f} is bigger than {num2:.2f} use "pctmore" instead')
    if float(result).is_integer():
        return (f'{num1:.2f} is {result:.2f}% less than {num2:.2f}')
    else:
      return (f'{num1:.2f} is {result:.2f}% less than {num2:.2f}')

if __name__ == '__main__':
  fire.Fire(Pycenter)
