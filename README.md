![Wagg Logo](assets/wagg.png)  
  
-----------------------------  
  
Wagg programming language interpreter tippy tapped in Go/Python


![](https://github.com/HarryMills/Wagg/workflows/.github/workflows/python-app.yml/badge.svg)

### Features  

 - C-like syntax in Doggo Language!
 - Variable bindings (Boops)
 - Integers (Puppers) and Booleans (Bois)
 - Arithmetic expressions
 - Built-in functions (Floofs)
 - First-class and higher-order floofs
 - Closures
 - A string (Woofer) data structure
 - An array (Doggo) data structure
 - A hash (Yapper) data structure

  
#### What does Wagg look like?  
  
Binding Values to Names:  
  
	boop age = 1; 
	boop name = "Wagg"; 
	boop result = 10 * (20 / 2);  

Doggo support:

	boop myDoggo = [1, 2, 3, 4, 5];

Yapper support:

	boop lucky = {"name": "Lucky", "age": 2};

Accessing elements in Doggos and Yappers are done with index expressions:

	myDoggo[0]      // => 1
	lucky["name"]   // => "Lucky"

Boop can also be used to bind floofs to names:  
	
	boop add = floof(a, b) {bork a + b; };

Calling the floof:

	add(1, 2);

More complex floof:

	boop fibonacci = floof(x) {
		mlem (x == 0) {
			bork 0;
		} blep {
			mlem (x == 1) {
				bork 1;
			} blep {
				fibonacci(x - 1) + fibonacci(x - 2);
			}
		}
	};
