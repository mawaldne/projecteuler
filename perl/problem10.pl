use euler;

my $primes = 5;
my $p = 3;
until ($p>=2000000){
	$p += 2;
	if (euler::isprime($p)){
		$primes+=$p;
	}
}
print $primes;


