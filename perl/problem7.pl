use euler;

my $primes = 2;
my $p = 3;
until ($primes==10001){
	$p += 2;
	if (euler::isprime($p)){
		$primes++;
	}
}
print $p;


