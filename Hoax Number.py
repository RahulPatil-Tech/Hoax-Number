import math 
def primeFactors(n) : 
  result = [] 
  if (n % 2 == 0) : 
    while (n % 2 == 0) : 
      n = int(n / 2) 
    result.append(2) 
  for i in range(3,int(math.sqrt(n)),2): 
    if (n % i == 0) : 
      while (n % i == 0) : 
        n = int(n / i) 
      result.append(i) 
  if (n > 2) : 
    result.append(n) 
  return result 
def isHoax(n) :  
  p_fac = primeFactors(n) 
  if (p_fac[0] == n) : 
    return False
  all_pf_sum = 0
  for i in range(0,len(p_fac)):  
    pf_sum = 0
    while (p_fac[i] > 0): 
      pf_sum += p_fac[i] % 10
      p_fac[i] = int(p_fac[i] / 10) 
    all_pf_sum += pf_sum 
  sum_Ndigits = 0; 
  while (n > 0): 
    sum_Ndigits += n % 10
    n = int(n / 10) 
  return sum_Ndigits == all_pf_sum 
n = int(input("Enter the n value: ")); 
if (isHoax(n)): 
  print ("n is a Hoax Number") 
else: 
  print ("n is not a Hoax Number")
