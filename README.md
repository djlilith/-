## компилятор java на python
### авторы: Долгушина Анна, Голубева Дарья, Эл Хаджари Фатима-Эззахра

----
### 1 Аттестация
Входные данные:
```
class Example {
    int x;
    String name;

    void methodWithoutParams() {
        int y = 10;
    }

    int methodWithParams(int a, String b) {
        return a;
    }

    public static void main(String[] args) {
        Example e = new Example();
        e.methodWithoutParams();
        int result = e.methodWithParams(5, "test");
    }
}
```
Выходные данные:
```
================================================== Abstract Syntax Tree ==================================================
Program
├ ClassDef
  │ └ class
  │ └ Example
  │ └ {
  ├ FieldDecl
  │ ├ Type
  │ │ ├ PrimitiveType
  │ │     └ int
  │ │ └ x
  │   └ ;
  ├ FieldDecl
  │ ├ Type
  │ │ ├ ClassType
  │ │     └ String
  │ │ └ name
  │   └ ;
  ├ MethodDecl
  │ ├ Type
  │ │ ├ PrimitiveType
  │ │     └ void
  │ │ └ methodWithoutParams
  │ │ └ (
  │ │ └ )
  │ ├ Block
  │   │ └ {
  │   ├ Statement
  │   │ ├ VarDecl
  │   │ │ ├ Type
  │   │ │ │ ├ PrimitiveType
  │   │ │ │     └ int
  │   │ │ │ └ y
  │   │ │ │ └ =
  │   │ │ ├ PrimaryExpr
  │   │ │   ├ Primary
  │   │ │       └ 10
  │   │   └ ;
  │     └ }
  ├ MethodDecl
  │ ├ Type
  │ │ ├ PrimitiveType
  │ │     └ int
  │ │ └ methodWithParams
  │ │ └ (
  │ ├ Params
  │ │ ├ Param
  │ │ │ ├ Type
  │ │ │ │ ├ PrimitiveType
  │ │ │ │     └ int
  │ │ │   └ a
  │ │ │ └ ,
  │ │ ├ Param
  │ │   ├ Type
  │ │   │ ├ ClassType
  │ │   │     └ String
  │ │     └ b
  │ │ └ )
  │ ├ Block
  │   │ └ {
  │   ├ Statement
  │   │ │ └ return
  │   │ ├ PrimaryExpr
  │   │ │ ├ Primary
  │   │ │     └ a
  │   │   └ ;
  │     └ }
  ├ MethodDecl
  │ ├ Modifier
  │ │   └ public
  │ ├ Modifier
  │ │   └ static
  │ ├ Type
  │ │ ├ PrimitiveType
  │ │     └ void
  │ │ └ main
  │ │ └ (
  │ ├ Params
  │ │ ├ Param
  │ │   ├ Type
  │ │   │ ├ ArrayType
  │ │   │   ├ ClassType
  │ │   │   │   └ String
  │ │   │   │ └ [
  │ │   │     └ ]
  │ │     └ args
  │ │ └ )
  │ ├ Block
  │   │ └ {
  │   ├ Statement
  │   │ ├ VarDecl
  │   │ │ ├ Type
  │   │ │ │ ├ ClassType
  │   │ │ │     └ Example
  │   │ │ │ └ e
  │   │ │ │ └ =
  │   │ │ ├ NewExpr
  │   │ │   │ └ new
  │   │ │   ├ ClassCreator
  │   │ │     ├ ClassType
  │   │ │     │   └ Example
  │   │ │     │ └ (
  │   │ │       └ )
  │   │   └ ;
  │   ├ Statement
  │   │ ├ MethodCall
  │   │ │ ├ PrimaryExpr
  │   │ │ │ ├ Primary
  │   │ │ │     └ e
  │   │ │ │ └ .
  │   │ │ │ └ methodWithoutParams
  │   │ │ │ └ (
  │   │ │   └ )
  │   │   └ ;
  │   ├ Statement
  │   │ ├ VarDecl
  │   │ │ ├ Type
  │   │ │ │ ├ PrimitiveType
  │   │ │ │     └ int
  │   │ │ │ └ result
  │   │ │ │ └ =
  │   │ │ ├ MethodCallExpr
  │   │ │   ├ PrimaryExpr
  │   │ │   │ ├ Primary
  │   │ │   │     └ e
  │   │ │   │ └ .
  │   │ │   │ └ methodWithParams
  │   │ │   │ └ (
  │   │ │   ├ PrimaryExpr
  │   │ │   │ ├ Primary
  │   │ │   │     └ 5
  │   │ │   │ └ ,
  │   │ │   ├ PrimaryExpr
  │   │ │   │ ├ Primary
  │   │ │   │     └ "test"
  │   │ │     └ )
  │   │   └ ;
  │     └ }
    └ }
  └ <EOF>
====================================================================================================
```
----
