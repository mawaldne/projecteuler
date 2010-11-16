my $div = 20;
while(1){
	my $divisible = 1;
	for (11..20){ 
		unless ($div % $_ == 0){ 
			$divisible = 0;
		} 
		unless ($divisible){
			last;
		}
	}
	if ($divisible){
		last;
	}
	$div += 20;
}
print $div;