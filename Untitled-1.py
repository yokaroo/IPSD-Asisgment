def is_prime(n):
  """Mengembalikan True jika n adalah bilangan prima, False jika tidak."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


def prime_pattern(num_rows):
  """Menghasilkan pola bilangan prima."""
  primes = []
  num = 2
  while len(primes) < (num_rows * (num_rows + 1)) // 2:  # Jumlah total bilangan prima yang dibutuhkan
    if is_prime(num):
      primes.append(num)
    num += 1
  
  index = 0
  for i in range(1, num_rows + 1):
    row = []
    for j in range(i):
      row.append(primes[index])
      index += 1
    print(*row)


# Contoh penggunaan:
num_rows = 4
prime_pattern(num_rows)
