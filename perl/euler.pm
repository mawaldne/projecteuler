package euler;

sub isprime{
	my $p = shift;
	return 1 if ($p == 2);
	return 0 if ($p < 2 || $p % 2 == 0);

	my $i = 3;
	my $max = int($p**0.5) + 1;
	while ($i < $max){
		return 0 if ($p % $i == 0);
		$i+=2;
	}
	return 1;
}

sub ispalindrome {
	my $pal = shift;
	return $pal == reverse $pal;
}

1;