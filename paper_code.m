syms x0 x1 x2 x3
%arr = [-0.105,0.227,0.357,0.818,-0.777,-0.37,-0.061,-0.758,0.708,-0.279];
arr = [0.943,-0.565,-0.425,-0.699,0.339,-0.84,0.454,0.049,-0.852,0.507,0.185,0.513,-0.169,0.705,-0.967]; %long one
%arr = [-0.409,-0.622,0.405,0.108,-0.984,0.286,-0.342,-0.677,0.033,-0.207,-0.804,-0.036,0.689,0.525,-0.663];
%terms = [x0*x0, x0*x1, x0*x2, x0, x1*x1, x1*x2, x1, x2*x2, x2, 1];
terms = [x0*x0, x0*x1, x0*x2, x0*x3, x0, x1*x1, x1*x2, x1*x3, x1, x2*x2, x2*x3, x2, x3*x3, x3, 1];
fun_array = sym('fi',[1 length(arr)])
for i = 1:length(arr)
    fun_array(i) = double(arr(i))*terms(i);
end
f = sum(fun_array)
double(eig(hessian(f,[x0,x1,x2,x3])))
x = [x0;x1;x2;x3];
gradf = jacobian(f,x).'
hessf = jacobian(gradf,x)
fh = matlabFunction(f,gradf,hessf,'vars',{x});
[V,D,W] = eig(hessf);
double(V)
double(D)
double(W)