import ast
import astor

class DynamicCodeGenerator:
    @staticmethod
    def generate_function_code(function_name, function_class):
        """Dynamically generate executable Python code"""
        try:

            method = getattr(function_class, function_name)
            
            main_func = ast.FunctionDef(
                name='main',
                args=ast.arguments(
                    posonlyargs=[],
                    args=[],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[]
                ),
                body=[
                    ast.Try(
                        body=[
                            ast.Assign(
                                targets=[ast.Name(id='result', ctx=ast.Store())],
                                value=ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Name(id='SystemFunctions', ctx=ast.Load()),
                                        attr=function_name,
                                        ctx=ast.Load()
                                    ),
                                    args=[],
                                    keywords=[]
                                )
                            ),
                            ast.Expr(
                                value=ast.Call(
                                    func=ast.Name(id='print', ctx=ast.Load()),
                                    args=[
                                        ast.JoinedStr(
                                            values=[
                                                ast.Constant(value=f'{function_name} result: '),
                                                ast.FormattedValue(
                                                    value=ast.Name(id='result', ctx=ast.Load()),
                                                    conversion=-1
                                                )
                                            ]
                                        )
                                    ],
                                    keywords=[]
                                )
                            )
                        ],
                        handlers=[
                            ast.ExceptHandler(
                                type=ast.Name(id='Exception', ctx=ast.Load()),
                                name='e',
                                body=[
                                    ast.Expr(
                                        value=ast.Call(
                                            func=ast.Name(id='print', ctx=ast.Load()),
                                            args=[
                                                ast.JoinedStr(
                                                    values=[
                                                        ast.Constant(value='Error executing function: '),
                                                        ast.FormattedValue(value=ast.Name(id='e', ctx=ast.Load()), conversion=-1)
                                                    ]
                                                )
                                            ],
                                            keywords=[]
                                        )
                                    )
                                ]
                            )
                        ],
                        finalbody=[],
                        orelse=[]
                    )
                ],
                decorator_list=[]
            )
            
            module = ast.Module(
                body=[
                    ast.ImportFrom(
                        module='automation_functions.system_functions',
                        names=[ast.alias(name='SystemFunctions', asname=None)],
                        level=0
                    ),
                    main_func,
                    ast.If(
                        test=ast.Compare(
                            left=ast.Name(id='__name__', ctx=ast.Load()),
                            ops=[ast.Eq()],
                            comparators=[ast.Constant(value='__main__')]
                        ),
                        body=[
                            ast.Expr(
                                value=ast.Call(
                                    func=ast.Name(id='main', ctx=ast.Load()), 
                                    args=[], 
                                    keywords=[]
                                )
                            )
                        ],
                        orelse=[]
                    )
                ],
                type_ignores=[]
            )
            
            return astor.to_source(module)
        
        except Exception as e:
            return f"Error generating code: {str(e)}"