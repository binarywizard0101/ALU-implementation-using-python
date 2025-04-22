# ALU-implementation-using-python
As a passionate learner of computer architecture, I created this project to explore how basic instruction processing, arithmetic operations, and flag handling work in a simulated environment. This project helps visualize how a CPU handles addition, subtraction, bitwise operations, and flag setting in a simple register-based system.
# Features
✅ Supports basic arithmetic operations (ADD, SUB) 
✅ Includes bitwise operations (AND, OR, XOR) 
✅ Implements flag handling (Carry, Zero, Parity) 
✅ Simulates memory storage for results
![alt text] https://lh3.googleusercontent.com/fife/ALs6j_FxXGyVbBf6SMvuePY-K2R0G8wgzIsPUAbJqPznwvcCzfDBQynjl22AJTyST-jWIvpC6S-IJTbli8j8dIJmbkG5QuWmjgcAxm33wOriU76h3tS6we4FrgYmREdNw4v0nEn8ImkKcKJ6mMR1YTR7QGQ2P9EFOYPjJ6byCNSWy3a2erCHHUpdvf33i6gO9-8D8y-fPVDYa0nBoZ3-BdqF49qnb3PZUZSuJrrSSaylqh99_W8KBIjacpU4Rj0IE0Lk3lxk3vTsf4XK5zYvvLTkok_c8rdaBxXGtU7_BahVeDPGV1J9qsssO5spZEuOpw8EziacFo8zyZ0wlUSCMJ2AfSrmgZH_6Kq5Y05PJs8T8vXokhwmD_Dz95rV-tXnN8U-RpVXYvNuxTOvuIFvdAd_fEJ9CSxYGO90rROQNM0rFBaulgbC34gzFzwjqxyN2R-UlPHDLp2BMAKZsMUfqRrBurBEHfHufTXT3nZNnT9AK-CX_iETPWqgd_heLPpUbaew2t5NmgptKsMYKxhb3XljOsligm7I63uVEsTf73V4MZ3ke62f93DUqYRkXR17aw1vXigy9nPxqmdwrixxgl1SwpAsZJQ0iIZkuzsArshnyNuXdOP-50eF3vChOPNQAojyzq_euBvtCvFkGFt9N0zaQuCrIYIfDOVYQskrhs63H5fBrrYJzW3KheaOO-WGkZo1ITz8ADVkzAob_NMX91VRWmJqDlpR6loZXsfASiXNe0vqdU3yy-1ypwviZlUdSWxO18N4l4sUFHuzvjuNXp7Z6nfly0ZqSSshTKkzVDdYgCERlauTGDRfH5RqU9b619LUgk8PnyGiEIvDSO09tbSdlobJYQofR4rcKFiBeJYwJZda9hxBGBSd36oxnGkij7CZgjaHbd8b1x2f0MFpKqnpNljEDI8R4ikyVkyzOsuQh0bHSHDM-5eRyZOX74OR9jp89672ilMc-hQjkUNMZur0sISyY6ZjwIT1VCpqkjym0UGDdj-NpDNOYhEyXgE3AcWlZHWpuIYAHe44BAzXygzttfQmDUjz3H2yDj7COj2ky8AIbHh_1AdxK6K6HHB0IYfwe6SVuri9Mb9GHO2x3hTOI-iy3vNtsNZz9EUgorZlia8panSThCBcD7tKWqVQel_PKSi9GIuz7ahO7zeAU4dEmN60dbXfLHybEmhAF8vzrNgrU2LeQBN0bM9sbsx-OVmgqSZabm7aaygdl2S4PjM6Tr7Z7FOqiYurit55Ca-_xlWaw_lufyRwQKlExXZlpHFA98zV0fOpk74ECf3MyI4XPEsW0jJOOimHrgcdTF7PTlXEAjmdY2QCCo8vqDnNjy8roosWJ3gSNKGyS_CY5BZmGLm2zHI50vl4uDyZUCyW6A-HikGsvDhgDF4xE7UazMYTGtanYuCJmklmnG-aDPqyp2_iIrMZgO95Xdd8G6RH58dgShK4PNShPu_jyRdEPJYApfTRxZOP2y9NLYpINAGuQdYS4bH_As5V6PPl0Nbv1J4XbPwZaMYBsUe2R9UaXvzQU0Fq6Ze7M_PNK0Zho9WhwekCFQUSxhJ4AoNDGkpBcxxki66BbkRa-rnYnX4sNc3FLKHPA-w1hQCr6B9_eNcPqUTVzGGp3gieCveKCPjKmSuxjytbyl62H_IQ1NN1OU6DVWOZYdPl7ESHc242WUqVonuTGn4=w1863-h877?auditContext=forDisplay
# Instructions
The ALU accepts three instructions sequentially:

Loading Values

LOAD R1: Loads a value into register R1

LOAD R2: Loads a value into register R2

Storing Values

STORE R1 MEM: Stores the value of R1 into memory

STORE R2 MEM: Stores the value of R2 into memory

Arithmetic and Logic Operations

ADD: Adds values in R1 and R2

SUB: Subtracts R2 from R1

AND: Performs bitwise AND between R1 and R2

OR: Performs bitwise OR between R1 and R2

XOR: Performs bitwise XOR between R1 and R2

Flags are set based on the result:

Carry Flag (carry_flag): Set if the result exceeds a defined limit

Zero Flag (zero_flag): Set if the result is 0

Parity Flag (parity_flag): Set if the result is even
# Future Improvements
🔹 Adding multiplication & division operations 
🔹 Implementing overflow detection 
🔹 Enhancing memory management and addressing 
🔹 Extending support for more instructions
