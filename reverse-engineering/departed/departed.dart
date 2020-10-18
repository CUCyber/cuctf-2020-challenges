import 'dart:convert';
import 'dart:io';

final List<int> flag = [
  67,
  85,
  67,
  84,
  70,
  123,
  101,
  86,
  51,
  114,
  89,
  48,
  110,
  51,
  95,
  108,
  111,
  86,
  51,
  115,
  95,
  117,
  110,
  80,
  48,
  112,
  85,
  108,
  52,
  114,
  95,
  108,
  52,
  110,
  103,
  117,
  97,
  71,
  51,
  115,
  125
];

void main() {
  print("Enter the flag: ");
  List<int> input = stdin.readLineSync(encoding: latin1).codeUnits;

  if (input.length != flag.length) {
    print("Nope, not flag");
    return;
  }

  for (int i = 0; i < flag.length; i++) {
    if (input[i] != flag[i]) {
      print("Nope, not flag");
      return;
    }
  }

  StringBuffer newFlag = new StringBuffer();
  input.forEach((e) {
    newFlag.writeCharCode(e);
  });

  print("YAY ${newFlag.toString()} is the flag!!!");
}
