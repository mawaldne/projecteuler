use euler;

my $max = 0;
for my $x (100..999) {
	for my $y ($x..999) {
		$p = $x * $y;
		if ($p > $max && euler::ispalindrome($p))
		{
			$max = $p;
		}
	}
}

print $max . "\n";

