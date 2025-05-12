# Generated from JavaSubset.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JavaSubsetParser import JavaSubsetParser
else:
    from JavaSubsetParser import JavaSubsetParser

# This class defines a complete listener for a parse tree produced by JavaSubsetParser.
class JavaSubsetListener(ParseTreeListener):

    # Enter a parse tree produced by JavaSubsetParser#program.
    def enterProgram(self, ctx:JavaSubsetParser.ProgramContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#program.
    def exitProgram(self, ctx:JavaSubsetParser.ProgramContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#classDef.
    def enterClassDef(self, ctx:JavaSubsetParser.ClassDefContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#classDef.
    def exitClassDef(self, ctx:JavaSubsetParser.ClassDefContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#fieldDecl.
    def enterFieldDecl(self, ctx:JavaSubsetParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#fieldDecl.
    def exitFieldDecl(self, ctx:JavaSubsetParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#methodDecl.
    def enterMethodDecl(self, ctx:JavaSubsetParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#methodDecl.
    def exitMethodDecl(self, ctx:JavaSubsetParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#modifier.
    def enterModifier(self, ctx:JavaSubsetParser.ModifierContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#modifier.
    def exitModifier(self, ctx:JavaSubsetParser.ModifierContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#params.
    def enterParams(self, ctx:JavaSubsetParser.ParamsContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#params.
    def exitParams(self, ctx:JavaSubsetParser.ParamsContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#param.
    def enterParam(self, ctx:JavaSubsetParser.ParamContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#param.
    def exitParam(self, ctx:JavaSubsetParser.ParamContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#type.
    def enterType(self, ctx:JavaSubsetParser.TypeContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#type.
    def exitType(self, ctx:JavaSubsetParser.TypeContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#primitiveType.
    def enterPrimitiveType(self, ctx:JavaSubsetParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#primitiveType.
    def exitPrimitiveType(self, ctx:JavaSubsetParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#classType.
    def enterClassType(self, ctx:JavaSubsetParser.ClassTypeContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#classType.
    def exitClassType(self, ctx:JavaSubsetParser.ClassTypeContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#arrayType.
    def enterArrayType(self, ctx:JavaSubsetParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#arrayType.
    def exitArrayType(self, ctx:JavaSubsetParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#block.
    def enterBlock(self, ctx:JavaSubsetParser.BlockContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#block.
    def exitBlock(self, ctx:JavaSubsetParser.BlockContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#statement.
    def enterStatement(self, ctx:JavaSubsetParser.StatementContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#statement.
    def exitStatement(self, ctx:JavaSubsetParser.StatementContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#forControl.
    def enterForControl(self, ctx:JavaSubsetParser.ForControlContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#forControl.
    def exitForControl(self, ctx:JavaSubsetParser.ForControlContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#printStmt.
    def enterPrintStmt(self, ctx:JavaSubsetParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#printStmt.
    def exitPrintStmt(self, ctx:JavaSubsetParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#varDecl.
    def enterVarDecl(self, ctx:JavaSubsetParser.VarDeclContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#varDecl.
    def exitVarDecl(self, ctx:JavaSubsetParser.VarDeclContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#assignment.
    def enterAssignment(self, ctx:JavaSubsetParser.AssignmentContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#assignment.
    def exitAssignment(self, ctx:JavaSubsetParser.AssignmentContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#lhs.
    def enterLhs(self, ctx:JavaSubsetParser.LhsContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#lhs.
    def exitLhs(self, ctx:JavaSubsetParser.LhsContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#methodCall.
    def enterMethodCall(self, ctx:JavaSubsetParser.MethodCallContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#methodCall.
    def exitMethodCall(self, ctx:JavaSubsetParser.MethodCallContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#newExpr.
    def enterNewExpr(self, ctx:JavaSubsetParser.NewExprContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#newExpr.
    def exitNewExpr(self, ctx:JavaSubsetParser.NewExprContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#mulDivMod.
    def enterMulDivMod(self, ctx:JavaSubsetParser.MulDivModContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#mulDivMod.
    def exitMulDivMod(self, ctx:JavaSubsetParser.MulDivModContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#methodCallExpr.
    def enterMethodCallExpr(self, ctx:JavaSubsetParser.MethodCallExprContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#methodCallExpr.
    def exitMethodCallExpr(self, ctx:JavaSubsetParser.MethodCallExprContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#notExpr.
    def enterNotExpr(self, ctx:JavaSubsetParser.NotExprContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#notExpr.
    def exitNotExpr(self, ctx:JavaSubsetParser.NotExprContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#comparison.
    def enterComparison(self, ctx:JavaSubsetParser.ComparisonContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#comparison.
    def exitComparison(self, ctx:JavaSubsetParser.ComparisonContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:JavaSubsetParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:JavaSubsetParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#unaryMinus.
    def enterUnaryMinus(self, ctx:JavaSubsetParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#unaryMinus.
    def exitUnaryMinus(self, ctx:JavaSubsetParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#logicalAnd.
    def enterLogicalAnd(self, ctx:JavaSubsetParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#logicalAnd.
    def exitLogicalAnd(self, ctx:JavaSubsetParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#addSub.
    def enterAddSub(self, ctx:JavaSubsetParser.AddSubContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#addSub.
    def exitAddSub(self, ctx:JavaSubsetParser.AddSubContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#arrayIndexExpr.
    def enterArrayIndexExpr(self, ctx:JavaSubsetParser.ArrayIndexExprContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#arrayIndexExpr.
    def exitArrayIndexExpr(self, ctx:JavaSubsetParser.ArrayIndexExprContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#logicalOr.
    def enterLogicalOr(self, ctx:JavaSubsetParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#logicalOr.
    def exitLogicalOr(self, ctx:JavaSubsetParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#equality.
    def enterEquality(self, ctx:JavaSubsetParser.EqualityContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#equality.
    def exitEquality(self, ctx:JavaSubsetParser.EqualityContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#classCreator.
    def enterClassCreator(self, ctx:JavaSubsetParser.ClassCreatorContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#classCreator.
    def exitClassCreator(self, ctx:JavaSubsetParser.ClassCreatorContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#arrayCreator.
    def enterArrayCreator(self, ctx:JavaSubsetParser.ArrayCreatorContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#arrayCreator.
    def exitArrayCreator(self, ctx:JavaSubsetParser.ArrayCreatorContext):
        pass


    # Enter a parse tree produced by JavaSubsetParser#primary.
    def enterPrimary(self, ctx:JavaSubsetParser.PrimaryContext):
        pass

    # Exit a parse tree produced by JavaSubsetParser#primary.
    def exitPrimary(self, ctx:JavaSubsetParser.PrimaryContext):
        pass



del JavaSubsetParser