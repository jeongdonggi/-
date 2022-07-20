# 1. 문자열 압축
알파벳 대문자로 이루어진 문자열을 입력받아 같은 문자가 연속으로 반복되는 경우 반복되는 문자 바로 오른쪽에 반복 횟수를 표기하는 방법으로 문자열을 압축하는 프로그램을 작성하세요. 단 반복횟수가 1인 경우 생략합니다.

<strong>알고리즘</strong><br>
알파벳의 옆이 같을 때 count를 올려주는 방법을 이용한다. 맨 마지막 알파벳은 비교할 대상이 없으므로 빈칸을 채워준다.

<strong>핵심 코드(자바)</strong><br>
```java
if(s.charAt(i) == s.charAt(i+1)){ //문자열을 하나씩 비교해준다.
  count++;
}
```
<strong>핵심 코드(파이썬)</strong><br>
```python
if(s[i] == s[i+1]){
  count+=1
}
```
# 2. 회문 문자열
앞에서 읽을 때나 뒤에서 읽을 때나 같은 문자열을 회문 문자열이라고 합니다. 문자열이 입력되면 해당 문자열이 회문 문자열이면 "YES", 회문 문자열이 아니면 "NO"를 출력하는 프로그램을 작성하세요.
단, 회문을 검사할 때 대소문자를 구분하지 않습니다.

<strong>알고리즘</strong><br>
대소문자를 구분하지 않으므로 소문자나 대문자로 통일을 한다. 양쪽을 하나씩 검사하면서 틀린게 없다면 yes를 틀린게 있다면 no를 출력하게 한다.

<storng>핵심 코드(자바)</storng><br>
```java
s = s.toUpperCase(Locale.ROOT); //대문자 변환

left = 0;
right = s.length() - 1;
while (left<rignt)
```
<strong>핵심 코드(파이썬)</strong><br>
```python
s = s.upper() # 대문자 변환
```
<strong>알고리즘(쉬운 방법)</strong><br>
대문자로 변환 후 문자열의 순서를 반대로 바꾸어 원래 문자열과 비교를 한다.

<strong>핵심 코드(자바)</strong><br>
```java
String tmp = new StringBuilder(s).reverse().toString(); //변환 가능한 문자열로 바꾼 후 리버슬 해주고 다시 변환 불가한 문자열로 바꿈
if(s.equalsIgnoreCase(tmp)) answer = "YES"; //대소문자 구분 없이 문자열 구분 가능
```
<storng>핵심 코드(파이썬)</strong><br>
```python
s = s.upper()
if( s != s[::-1]):
  return "NO"
```

# 3. 특정 문자 뒤집기

<strong>알고리즘</strong><br>
