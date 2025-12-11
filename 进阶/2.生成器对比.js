// JavaScript版本 - 斐波那契数列生成器对比

// 1. 使用生成器函数 (ES6+)
function* fibonacci() {
    let a = 0, b = 1;
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
}

// 好处：
// 1. 惰性计算：按需生成值，节省内存
// 2. 无限序列：可以表示无限长的斐波那契数列  
// 3. 状态保持：自动记住执行状态
// 4. 可迭代：支持for...of循环和next()调用

// 示例：获取前10个斐波那契数
console.log("前10个斐波那契数:");
const fib = fibonacci();
for (let i = 0; i < 10; i++) {
    const { value } = fib.next();
    console.log(`F${i}: ${value}`);
}

// 也可以使用解构赋值
console.log(fib.next().value); // 0
console.log(fib.next().value); // 1  
console.log(fib.next().value); // 1
console.log(fib.next().value); // 2

// 2. 传统函数实现（对比）
function fibonacciTraditional(n) {
    let a = 0, b = 1;
    const result = [];
    for (let i = 0; i < n; i++) {
        result.push(a);
        [a, b] = [b, a + b];
    }
    return result;
}

console.log("传统方式前10个:", fibonacciTraditional(10));

// 3. 闭包实现（类似Python的生成器）
function fibonacciClosure() {
    let a = 0, b = 1;
    return {
        next: function() {
            const value = a;
            [a, b] = [b, a + b];
            return { value, done: false };
        }
    };
}

const closureFib = fibonacciClosure();
console.log("闭包实现:");
console.log(closureFib.next().value); // 0
console.log(closureFib.next().value); // 1

// 4. 生成器表达式对比
// Python: squares = (x**2 for x in range(10))
// JavaScript等效写法：
function* squaresGen() {
    for (let x = 0; x < 10; x++) {
        yield x * x;
    }
}

console.log("前5个平方数:");
const squares = squaresGen();
for (let i = 0; i < 5; i++) {
    const { value } = squares.next();
    console.log(`Square ${i}: ${value}`);
}

// 5. 数组方法实现（更符合JS习惯）
const squaresArray = Array.from({length: 10}, (_, i) => i * i);
console.log("数组方式前5个平方数:", squaresArray.slice(0, 5));

// 6. 异步生成器（JavaScript特有）
async function* asyncFibonacci() {
    let a = 0, b = 1;
    while (true) {
        await new Promise(resolve => setTimeout(resolve, 100)); // 模拟异步操作
        yield a;
        [a, b] = [b, a + b];
    }
}

// 使用异步生成器
(async () => {
    console.log("异步斐波那契:");
    const asyncFib = asyncFibonacci();
    for (let i = 0; i < 5; i++) {
        const { value } = await asyncFib.next();
        console.log(`Async F${i}: ${value}`);
    }
})();

// 7. 管道式处理对比
// Python风格的链式调用在JS中需要组合
function* filterEven(numbers) {
    for (const n of numbers) {
        if (n % 2 === 0) yield n;
    }
}

function* square(numbers) {
    for (const n of numbers) {
        yield n * n;
    }
}

// 使用管道
function* pipeline() {
    yield* square(filterEven(range(20)));
}

function* range(n) {
    for (let i = 0; i < n; i++) {
        yield i;
    }
}

console.log("管道处理结果:");
const pipelineResult = [];
for (const value of pipeline()) {
    pipelineResult.push(value);
}
console.log(pipelineResult); // [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]