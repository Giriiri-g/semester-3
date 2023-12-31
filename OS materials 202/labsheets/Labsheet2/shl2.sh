#!/bin/bash

cat > numericdata <<EOF
Karunagappally 34567 7864 6785
Kollam 56754 6754 7654
Vallikkavu 54328 7548 45675
Trivandrum 16423 6654 6754
Ernakulam 28796 8549 9875
Kayamkulam 35589 75892 3451
kottayam 45557 6773 6547
tirukulum 45675 56476 7896
EOF

echo -e "\n\nQuestion 2.a"
cat numericdata


echo -e "\n\nQuestion 2.b"
grep '^T' numericdata


echo -e "\n\nQuestion 2.c"
grep '^K' numericdata | cut -d " " -f 4 | sort -n


echo -e "\n\nQuestion 2.d"
cut -d " " -f 3 numericdata | grep -E '^6.*4$'


echo -e "\n\nQuestion 2.e"
cut -d " " -f 3 numericdata | grep -E '6+'


echo -e "\n\nQuestion 2.f"
cut -d " " -f 2 numericdata | grep -E '5+'
