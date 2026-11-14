grammar SquareEncoding;

// القاعدة الرئيسية: برنامج أو سلسلة معادلات
program: expression+ EOF ;

// العمليات الحسابية الممكنة بين المربعات
expression
    : square                     # SingleSquare
    | expression '+' expression  # AddExpr
    | expression '-' expression  # SubExpr
    | expression '*' expression  # MulExpr
    ;

// تعريف هيكل المربع الواحد (4 زوايا)
square
    : '[' topLeft=SYMBOL '|' topRight=SYMBOL ']'
      '[' bottomLeft=SYMBOL '|' bottomRight=SYMBOL ']'
    ;

// الرموز الأربعة المعتمدة في نظامك
SYMBOL : '—' | '.' | ',' | '*' ;

// تجاهل المسافات والأسطر الفارغة
WS : [ \t\r\n]+ -> skip ;
