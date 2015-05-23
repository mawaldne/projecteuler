def multiples(num)
  total = 0
  (0..num - 1).each do |n|
    if n % 3 == 0 || n % 5 == 0
      total += n
    end 
  end
  total
end 

multiples(1000) 
