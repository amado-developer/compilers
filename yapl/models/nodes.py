from yapl.models.context import Context
from yapl.models.types import Type, ContextType

"""
 Base node
"""

class Node:
    """
    AST base node
    """
    def __init__(self):
        self.context_type = ContextType()
        self.return_type = Type('Untype')
        self.dynamic_type = Type('Untype')
        self.inner_context = None
    
    def validate(self, context: Context) -> bool:
        """
        Validates AST, semantically correct
        :param context: Context to validate
        :return:
        """
        pass


"""
 YAPL nodes
"""
class ProgramNode(Node):
    def __init__(self, class_list):
        super(Node, self).__init__()
        self.class_list = class_list
        self.context = Context()
        self.context_map = {}
        self.initialize_context()
        self.initialize_builtin_types()

    def initialize_context(self):
        # Declaring the methods of Object
        self.context.functions['abort'] = []
        self.context.functions['type_name'] = []
        self.context.functions['copy'] = []

    def initialize_builtin_types(self):
        # Delare io
        io_context = self.context.create_child_context()
        io_context.functions['in_string'] = []
        io_context.functions['in_int'] = []
        io_context.functions['out_string'] = ['x']
        io_context.functions['out_int'] = ['x']
        self.context_map['IO'] = io_context

        int_context = self.context.create_child_context()
        self.context_map['Int'] = int_context

        string_context = self.context.create_child_context()
        self.context_map['String'] = string_context

        bool_context = self.context.create_child_context()
        self.context_map['Bool'] = bool_context

        object_context = self.context.create_child_context()
        self.context_map['Object'] = object_context

        self_type_context = self.context.create_child_context()
        self.context_map['SELF_TYPE'] = self_type_context

    def __repr__(self):
        s = "Program:\n"
        for c in self.class_list:
            s += str(c) + '\n'
        return s

    def validate(self, context_attributes_inheritance: ContextType, context: Context = None):
        # TODO: complete validation part
        return True


class ClassNode(Node):
    def __init__(self, name, parent, features):
        """
        :param name: The name of the class
        :param parent: The name of the parent class
        :param features: A list with the features of the class (methods and atributes)
        """
        super().__init__()
        self.name = name
        self.parent = parent
        self.features = features

    def __str__(self):
        return str(self.name)

    def validate(self, context) -> bool:
        # TODO: complete validation part
        return True


class FeatureNode(Node):
    def __init__(self):
        super().__init__()

    def validate(self, context: Context) -> bool:
        pass


class MethodNode(FeatureNode):
    def __init__(self, name, params, return_type, body):
        super().__init__()
        self.name = name
        self.params = params
        self.method_type = return_type
        self.body = body

    def validate(self, context: Context) -> bool:
        # TODO: complete validation part
        return True


class AttributeNode(FeatureNode):
    def __init__(self, name, attr_type, init_expr):
        super(AttributeNode, self).__init__()
        self.name = name
        self.attr_type = attr_type
        self.init_expr = init_expr

    def validate(self, context: Context) -> bool:
        # TODO: complete validation part
        return True


class ParamNode(FeatureNode):
    def __init__(self, name, param_type):
        super(ParamNode, self).__init__()
        self.name = name
        self.param_type = param_type

    def validate(self, context: Context):
        return True


class ObjectNode(Node):
    def __init__(self, name):
        super(ObjectNode, self).__init__()
        self.name = name

    def __str__(self):
        return self.name

    def validate(self, context: Context):
        # TODO: complete validation part
        return True


class SelfNode(ObjectNode):
    def __init__(self):
        super(SelfNode, self).__init__("SELF")


class ExpressionNode(Node):
    def __init__(self):
        super(ExpressionNode, self).__init__()

    @property
    def get_type(self):
        pass


class NewObjectNode(ExpressionNode):
    def __init__(self, new_type):
        super(NewObjectNode, self).__init__()
        self.type_new_object = new_type

    def validate(self, context: Context):
        return True


class CaseNode(ExpressionNode):
    def __init__(self, expr, actions):
        super(CaseNode, self).__init__()
        self.expr = expr
        self.actions = actions

    def validate(self, context: Context):
        # TODO: complete validation part
        return True


class ActionNode(Node):
    def __init__(self, name, action_type, body):
        super(ActionNode, self).__init__()
        self.name = name
        self.action_type = action_type
        self.body = body
        self.inner_context = None

    def validate(self, context: Context):
        self.inner_context = context.create_child_context()
        self.inner_context.define(self.name)
        return self.body.validate(self.inner_context)


class IsVoidNode(ExpressionNode):
    def __init__(self, expr: ExpressionNode):
        super(IsVoidNode, self).__init__()
        self.expr = expr

    @property
    def get_type(self):
        return 'Bool'

    def validate(self, context: Context):
        return self.expr.validate(context)


"""
 Operators
"""

class BinaryOperatorNode(ExpressionNode):
    def __init__(self, left: ExpressionNode, right: ExpressionNode):
        super(BinaryOperatorNode, self).__init__()
        self.left = left
        self.right = right

    @property
    def get_type(self):
        return self.left.get_type

    def validate(self, context: Context):
        return self.left.validate(context) and self.right.validate(context)


class UnaryOperator(ExpressionNode):
    def __init__(self, expr: ExpressionNode):
        super(UnaryOperator, self).__init__()
        self.expr = expr

    @property
    def get_type(self):
        return self.expr.get_type

    def validate(self, context: Context):
        return self.expr.validate(context)


class AtomicNode(ExpressionNode):
    def __init__(self):
        super(AtomicNode, self).__init__()


class PlusNode(BinaryOperatorNode):
    def __init__(self, left, right):
        super(PlusNode, self).__init__(left, right)
        self.left = left
        self.right = right
        self.operator = '+'


class MinusNode(BinaryOperatorNode):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.left = left
        self.right = right
        self.operator = '-'


class StarNode(BinaryOperatorNode):
    def __init__(self, left, right):
        super(StarNode, self).__init__(left, right)
        self.left = left
        self.right = right
        self.operator = '*'


class DivNode(BinaryOperatorNode):
    def __init__(self, left, right):
        super(DivNode, self).__init__(left, right)
        self.left = left
        self.right = right
        self.operator = '/'


class EqualNode(BinaryOperatorNode):
    def __init__(self, left, right):
        super(EqualNode, self).__init__(left, right)
        self.left = left
        self.right = right
        self.operator = '='


class LessThanNode(BinaryOperatorNode):
    def __init__(self, left, right):
        super(LessThanNode, self).__init__(left, right)
        self.left = left
        self.right = right
        self.operator = '<'


class LessEqualNode(BinaryOperatorNode):
    def __init__(self, left, right):
        super(LessEqualNode, self).__init__(left, right)
        self.left = left
        self.right = right
        self.operator = '<='


class NegationNode(UnaryOperator):
    def __init__(self, value):
        super(NegationNode, self).__init__(value)
        self.value = value


class BooleanNegation(NegationNode):
    def __init__(self, value):
        super(BooleanNegation, self).__init__(value)
        self.operator = "!"


class IntegerNegation(NegationNode):
    def __init__(self, value):
        super(IntegerNegation, self).__init__(value)
        self.operator = "~"


class LetInNode(AtomicNode):
    def __init__(self, return_type, declaration_list, expr):
        super(LetInNode, self).__init__()
        # self.instance = instance
        self.return_type = return_type
        self.declaration_list = declaration_list
        self.expr = expr

    def get_type(self):
        return self.expr.get_type

    def validate(self, context: Context):
        # TODO: complete validation part
        return True


class DeclarationNode(ExpressionNode):
    def __init__(self, idx_token, type_token, expr=None):
        super(ExpressionNode, self).__init__()
        self.idx_token = idx_token
        self.type_token = type_token
        self.expr = expr
        self.variable_info = None

    def get_type(self):
        return self.type_token

    def validate(self, context: Context):
        # TODO: complete validation part
        return True


class IfNode(ExpressionNode):
    def __init__(self, predicate, then_expr, else_expr):
        super(IfNode, self).__init__()
        self.predicate = predicate
        self.then_expr = then_expr
        self.else_expr = else_expr

    # Este no se usa
    def get_type(self):
        return self.then_expr

    def validate(self, context: Context):
        # TODO: complete validation part
        return True


class WhileNode(ExpressionNode):
    def __init__(self, predicate, expr):
        super(WhileNode, self).__init__()
        self.predicate = predicate
        self.expr = expr

    # Este no se usa
    def get_type(self):
        return self.expr.get_type

    def validate(self, context: Context):
        # TODO: complete validation part
        return True


class BlockNode(AtomicNode):
    def __init__(self, expr_list):
        super(BlockNode, self).__init__()
        self.expr_list = expr_list

    def validate(self, context: Context):
        # TODO: complete validation part
        return True


class AssignNode(AtomicNode):
    def __init__(self, idx_token, expr):
        super(AssignNode, self).__init__()
        self.idx_token = idx_token
        self.expr = expr
        self.variable_info = None

    def validate(self, context: Context):
        # TODO: complete validation part
        return True


class DynamicDispatchNode(ExpressionNode):
    def __init__(self, instance, method, arguments):
        super(DynamicDispatchNode, self).__init__()
        self.instance = instance
        self.method = method
        self.arguments = arguments

    def validate(self, context: Context):
        # TODO: complete validation part
        return True


class StaticDispatchNode(ExpressionNode):
    def __init__(self, instance, dispatch_type, method, arguments):
        super(StaticDispatchNode, self).__init__()
        self.instance = instance
        self.dispatch_type = dispatch_type
        self.method = method
        self.arguments = arguments

    def validate(self, context: Context):
        # TODO: complete validation part
        return True


class IntegerNode(AtomicNode):
    def __init__(self, integer_token):
        super(IntegerNode, self).__init__()
        self.integer_token = integer_token

    def validate(self, context: Context) -> bool:
        return True


class BooleanNode(AtomicNode):
    def __init__(self, boolean_token):
        super(BooleanNode, self).__init__()
        self.boolean_token = boolean_token

    def validate(self, context: Context) -> bool:
        return True


class StringNode(AtomicNode):
    def __init__(self, string_token):
        super(StringNode, self).__init__()
        self.string_token = string_token

    def validate(self, context: Context) -> bool:
        return True


class VariableNode(AtomicNode):
    def __init__(self, idx_token):
        super(VariableNode, self).__init__()
        self.idx_token = idx_token
        self.variable_info = None

    def validate(self, context: Context):
        return context.is_defined(self.idx_token)


class PrintIntegerNode(AtomicNode):
    def __init__(self, expr):
        super(PrintIntegerNode, self).__init__()
        self.expr = expr

    def validate(self, context: Context) -> bool:
        return True


class PrintStringNode(AtomicNode):
    def __init__(self, string_token):
        super(PrintStringNode, self).__init__()
        self.string_token = string_token

    def validate(self, context: Context) -> bool:
        return True


class ScanNode(AtomicNode):
    def __init__(self, method):
        self.method = method
        super(ScanNode, self).__init__()
        # TODO : Chequear si el scan node recibe ya el string a escanear

    def validate(self, context: Context) -> bool:
        return True

