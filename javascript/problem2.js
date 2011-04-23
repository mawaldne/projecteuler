var 
sys = require("sys"),

even = function(n) {
	return (n%2) ? false : true;
},

MAX_FIB = 4000000,

fn_1 = 0, fn_2 = 1, fn = 0, sum = 0; 

while (fn < MAX_FIB) {
	fn = fn_1 + fn_2;
	if (even(fn)){
		sum = sum + fn;
	}
	fn_1 = fn_2;
	fn_2 = fn;
}

sys.puts(sum);
