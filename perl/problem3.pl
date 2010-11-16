use List::Util qw(min max);

print max (primefactorization(600_851_475_143));

sub primefactorization {
	my $num = shift; 
	my $pf = 2;
	while($num > 1){
		if ($num % $pf == 0 and isprime($pf)) {
			push(@primefactors, $pf);
			$num = $num / $pf;
			$pf = 2;
		} else {
			$pf++;
		}
	}
	return @primefactors;
}

sub isprime(){
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

Another solution
#!/usr/bin/perl -w
use strict;
 
my $big_number = 600_851_475_143;
my $i = 0;
 
until($big_number==1){ ($big_number%(++$i)==0) && ($big_number /= $i);	}
 
print "\n result: ", $i;


#!/usr/bin/perl
# What is the largest prime factor of the number 600_851_475_143?
my $int = 600_851_475_143;
my $factor = 2;
 
while ( $factor++**2 < $int ) { $int % $factor or $int /= $factor }
print $int;


Alright, so I used Recipe 2.19 from the Perl Cookbook ;)