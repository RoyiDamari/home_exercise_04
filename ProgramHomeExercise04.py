#  Exercise 1
# True
a = 1
b = 1
if a == b:
    print(f"was True for {a} {b}");
else:
    print(f"was False for {a} {b}");

a = 2
b = 2
c = 2
d = 2
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

a = 5
b = 3
c = 2
d = 4
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

a = 3
b = 5
c = 2
d = 4
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

a = 8
b = 8
c = 6
d = 9
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

a = 7
b = 7
c = 7
d = 7
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

a = 20
b = 22
if a != b:
    print(f"was True for {a} {b}");
else:
    print(f"was False for {a} {b}");

a = 12
b = 12
c = 12
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}");
else:
    print(f"was False for {a} {b} {c}");

a = 13
b = 14
c = 15
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}");
else:
    print(f"was False for {a} {b} {c}");

a = 6
b = 3
c = 9
d = 2
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

# False
a = 1
b = 0
if a == b:
    print(f"was True for {a} {b}");
else:
    print(f"was False for {a} {b}");

a = 0
b = 0
c = 1
d = 1
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

a = 2
b = 4
c = 3
d = 5
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

a = 6
b = 9
c = 12
d = 11
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

a = 1
b = 0
c = 7
d = 8
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

a = 0
b = 0
c = 0
d = 0
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

a = 20
b = 20
if a != b:
    print(f"was True for {a} {b}");
else:
    print(f"was False for {a} {b}");

a = "Ran"
b = "Frida"
c = "Dave"
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}");
else:
    print(f"was False for {a} {b} {c}");

a = 6
b = 3
c = 8
d = 2
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}");
else:
    print(f"was False for {a} {b} {c} {d}");

# Exercise 2
# if 4 < 9? True
# if (2 * 3 + 4) * (7 + 7)? True
# if 18 + 18? True
# if 10 == 10? True
# if 10 == 10 and 20 == 30? False
# if 10 == 10 or 20 == 30? True
# if 20 == 30 or 10 == 10? True
# if not 3? False
# if 3? True
# if True and True? True
# if True and False? False
# if True or False? True
# if False or True? True
# if (not 10) and (10)? False
# if (not 10) and (not 10)? False
# if 5 != 5 and 5 == 5? False
# if 2 == 2 or 3 == 3? True
# if 2 == 2 and 3 == 3? True
# if 40 == 30 and 1 >= 4? False
# if 13 >= 3 or 47 >= 5? True

# Exercise 3 + Bonus question
temp: float = float(input("Please enter a temperature: "));
print("hot" if temp > 30 else "normal");

temp: float = float(input("Please enter a temperature: "));
print("freezing" if temp < 0 else "normal" if temp < 20 else "hot");

# Exercise 4
for i in range(10,21):
    print(i);

for i in range(10,21,2):
    print(i);

skip_num: int = int(input("Please enter the skipping number: "));
for i in range(10, 21, skip_num):
    print(i);

start_point: int = int(input("Please enter the start point: "));
end_point: int = int(input("Please enter the end point: "));
skip_num: int = int(input("Please enter the skipping number: "));
for i in range(start_point,end_point + 1, skip_num):
    print(i);

# Exercise 5 + Bonus question
iq_num: int = int(input("Please enter your IQ number: "));
count: int = 0;
sum: int = 0;
highest_num: int = iq_num;
lowest_num: int = iq_num;

while iq_num >= 30 and iq_num <= 300:
    if iq_num >= highest_num:
        highest_num = iq_num;
    else:
        highest_num = highest_num;

    if iq_num <= lowest_num:
        lowest_num = iq_num;
    else:
        lowest_num = lowest_num;

    sum += iq_num;
    count += 1;
    iq_num: int = int(input("Please enter your IQ number: "));

avg_iq: float = sum / count;
print(f"The average IQ of the group is {avg_iq:.2f}");
print(f"The highest IQ score of the group is {highest_num}");
print(f"The lowest IQ score of the group is {lowest_num}");
print("one year of python training has been completed...");

iq_num_new: int = int(input("Please enter your IQ number: "));
count_new: int = 0;
sum_new: int = 0;
highest_num_new: int = iq_num_new;
lowest_num_new: int = iq_num_new;

while iq_num_new >= 30 and iq_num_new <= 300:
    if iq_num_new >= highest_num_new:
        highest_num_new = iq_num_new;
    else:
        highest_num_new = highest_num_new;

    if iq_num_new <= lowest_num_new:
        lowest_num_new = iq_num_new;
    else:
        lowest_num_new = lowest_num_new;

    sum_new += iq_num_new;
    count_new += 1;
    iq_num_new: int = int(input("Please enter your IQ number: "));

avg_iq_new: float = sum_new / count_new;
diff: float = avg_iq_new - avg_iq
print(f"The average IQ of the group is {avg_iq_new:.2f}");
print(f"The difference in IQ score between the 2 groups is {diff:.2f}");
print(f"The highest IQ score of the group is {highest_num_new}");
print(f"The lowest IQ score of the group is {lowest_num_new}");

if highest_num_new > highest_num:
    print(f"The highest IQ score between the 2 groups is {highest_num_new}");
else:
    print(f"The highest IQ score between the 2 groups is {highest_num}");

if lowest_num_new > lowest_num:
    print(f"The lowest IQ score between the 2 groups is {lowest_num}");
else:
    print(f"The lowest IQ score between the 2 groups is {lowest_num_new}");

# Exercise 6 + Bonus question
while True:
    str_1: str = input("Please enter a string: ");
    str_2: str = input("Please enter another string: ");
    if str_1 == str_2:
        break
    else: print(f"{str_1} {str_2}");

last_str: str = "";
concat_str: str = "";
while True:
    new_str: str = input("Please enter a string: ");
    concat_str += new_str + " ";
    if last_str == new_str:
        break
    else:
        last_str = new_str;

print(f"{concat_str}");

