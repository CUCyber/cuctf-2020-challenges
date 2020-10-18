# Solution

You can either reverse it statically or dynamically. I will be doing it statically. I would reccommend using wabt and using wasm2c to get a nicer looking file to reverse.
(There's also wasabi? Idk I haven't used it.)

There's a whole bunch of initialization stuff at the start, you can skip all that. The important part starts after the "FUNC_PROLOGUE;" line.

Here is the first small chunk that we will inspect.
```
w2c_i0 = 448u;		<--- const we are checking against
w2c_l4 = w2c_i0;
w2c_i0 = 0u;
w2c_l5 = w2c_i0;
w2c_i0 = w2c_l3;
w2c_i1 = w2c_p0;
i32_store(Z_envZ_memory, (u64)(w2c_i0) + 12, w2c_i1);
w2c_i0 = w2c_l3;
w2c_i1 = w2c_l5;
i32_store(Z_envZ_memory, (u64)(w2c_i0) + 8, w2c_i1);
w2c_i0 = w2c_l3;
w2c_i0 = i32_load(Z_envZ_memory, (u64)(w2c_i0) + 12u);		<--- always contains this line first, can ignore
w2c_l6 = w2c_i0;
w2c_i0 = w2c_l6;
w2c_i0 = i32_load8_u(Z_envZ_memory, (u64)(w2c_i0) + 12u);	<--- actual accessing our input[12]
w2c_l7 = w2c_i0;
w2c_i0 = 24u;
w2c_l8 = w2c_i0;
w2c_i0 = w2c_l7;
w2c_i1 = w2c_l8;
w2c_i0 <<= (w2c_i1 & 31);		<--- really weird wasm stuff ----
w2c_l9 = w2c_i0;							|
w2c_i0 = w2c_l9;							|
w2c_i1 = w2c_l8;							|
w2c_i0 = (u32)((s32)w2c_i0 >> (w2c_i1 & 31));		<----------------
w2c_l10 = w2c_i0;
w2c_i0 = w2c_l3;
w2c_i0 = i32_load(Z_envZ_memory, (u64)(w2c_i0) + 12u);		<--- ignore this line again
w2c_l11 = w2c_i0;
w2c_i0 = w2c_l11;
w2c_i0 = i32_load8_u(Z_envZ_memory, (u64)(w2c_i0) + 9u);	<--- actual accessing our input[9]
w2c_l12 = w2c_i0;
w2c_i0 = 24u;
w2c_l13 = w2c_i0;
w2c_i0 = w2c_l12;
w2c_i1 = w2c_l13;
w2c_i0 <<= (w2c_i1 & 31);		<--- ignore weird wasm stuff again
w2c_l14 = w2c_i0;
w2c_i0 = w2c_l14;
w2c_i1 = w2c_l13;
w2c_i0 = (u32)((s32)w2c_i0 >> (w2c_i1 & 31));
w2c_l15 = w2c_i0;
w2c_i0 = w2c_l10;
w2c_i1 = w2c_l15;
w2c_i0 += w2c_i1;			<---- adding w2c_l10 and w2c_l15

[truncated]
```

You get the idea. A bunch of random items in the input array are getting added up.
I commented all the key parts, but there are a bunch of these blocks in the wasm file. Then there are if statements, checking if all the numbers add up to the constant from the start. You can make a z3 script to solve.
