my $big_number = 600_851_475_143;
my $i = 0;
 
until($big_number==1){ ($big_number%(++$i)==0) && ($big_number /= $i);	}
 
print "$i\n";


my $int = 600_851_475_143;
my $factor = 2;
 
while ( $factor++**2 < $int ) { $int % $factor or $int /= $factor }
print "$int\n";