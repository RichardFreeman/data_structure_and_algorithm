def getTrains(n)
  if n < 2
    return 1
  end

  (0..(n-1)).inject(0) do |init, x|
    init + getTrains(x) * getTrains(n-x-1)
  end

end
