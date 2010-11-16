my $UPPER = 2_000_000;
    my $sieve = "";
    GUESS: for (my $guess = 2; $guess <= $UPPER; $guess++) {
      next GUESS if vec($sieve,$guess,1);
      $sum += $guess; 
      for (my $mults = $guess * $guess; $mults <= $UPPER; $mults += $guess) {
        vec($sieve,$mults,1) = 1;
      }
    }
print $sum;
