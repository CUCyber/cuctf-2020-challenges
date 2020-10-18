#include<emscripten.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdint.h>

EM_JS(char *, getString, (const char* str), {
    var retVal = UTF8ToString(str);
    var length = lengthBytesUTF8(retVal)+1;
    var result = _malloc(length);
    stringToUTF8(retVal, result, length);

    return result;
})

EM_JS(void, fail, (), {
    document.getElementById("answer").innerHTML = "<center>&#x1F47A</center>";
})

EM_JS(void, win, (), {
    document.getElementById("answer").innerHTML = "<center>&#x1F920</center>";
})

EMSCRIPTEN_KEEPALIVE
void check_coupon(const char *coupon)
{
    int checks = 0;

    if (coupon[14]+coupon[22] == 228) checks++;
    if (coupon[5]+coupon[13]+coupon[16]+coupon[19]+coupon[14]+coupon[9] == 605) checks++;
    if (coupon[18]+coupon[7]+coupon[17]+coupon[21]+coupon[2]+coupon[20] == 458) checks++;
    if (coupon[20]+coupon[20]+coupon[2]+coupon[16]+coupon[3]+coupon[11] == 507) checks++;
    if (coupon[12]+coupon[11]+coupon[15] == 250) checks++;
    if (coupon[20]+coupon[8]+coupon[15]+coupon[19]+coupon[4]+coupon[12]+coupon[13] == 655) checks++;
    if (coupon[1]+coupon[10]+coupon[16]+coupon[17]+coupon[9]+coupon[11]+coupon[4] == 564) checks++;
    if (coupon[22]+coupon[9]+coupon[13]+coupon[15] == 439) checks++;
    if (coupon[9]+coupon[3]+coupon[20]+coupon[11]+coupon[0] == 465) checks++;
    if (coupon[8]+coupon[13]+coupon[8]+coupon[9]+coupon[18]+coupon[18] == 523) checks++;
    if (coupon[15]+coupon[11]+coupon[9]+coupon[18]+coupon[5]+coupon[20]+coupon[18] == 606) checks++;
    if (coupon[1]+coupon[20]+coupon[5]+coupon[3]+coupon[4]+coupon[8] == 579) checks++;
    if (coupon[3]+coupon[11]+coupon[10]+coupon[15]+coupon[6] == 496) checks++;
    if (coupon[14]+coupon[11]+coupon[0]+coupon[0]+coupon[22]+coupon[5]+coupon[0] == 655) checks++;
    if (coupon[21]+coupon[8]+coupon[0]+coupon[15] == 379) checks++;
    if (coupon[16]+coupon[12]+coupon[17]+coupon[16] == 203) checks++;
    if (coupon[15]+coupon[3]+coupon[13]+coupon[15] == 384) checks++;
    if (coupon[7]+coupon[0]+coupon[4]+coupon[2]+coupon[16] == 350) checks++;
    if (coupon[4]+coupon[18]+coupon[11]+coupon[6] == 329) checks++;
    if (coupon[21]+coupon[3]+coupon[6]+coupon[12]+coupon[16]+coupon[2] == 473) checks++;
    if (coupon[4]+coupon[3]+coupon[6]+coupon[10]+coupon[22]+coupon[3]+coupon[12] == 629) checks++;
    if (coupon[1]+coupon[16]+coupon[12]+coupon[21]+coupon[2]+coupon[2] == 422) checks++;
    if (coupon[22]+coupon[19]+coupon[14] == 339) checks++;

    if(checks == 23)
    {
	win();
	return;
    }
    fail();
    return;
}
