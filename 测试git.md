## 长安十二时辰

### 右相的话

1. 年轻人总是不懂得一个道理，话不是说出来就有用的，要看听话的人愿不愿意听。
2. 插播，Git 中中文默认显示为八进制的字符编码，要想正确显示中文，使用如下代码
   git config --global core.quotepath false
3. 没有解决办法也敢来汇报。
4. 看一个人有没有本事，要看他 **得谁重用，与谁为敌**。
5. 稍微修改，看设置 GIt Bash 中的 Local 为中文,字符集为 UTF-8,看是否可以解决 git status 中文显示问题,在本测试之前,我已经将 git config --global core.quotepath false 语句设置为 true.
6. 实测只是修改 Git Bash 中的语言及字符集,不能解决 git status 中文问题,尽管我已经将 之前的 git...false 语句设置了为 true,不过我在新电脑上还是应该 在设置 false 之前,再测试一下再死心.实测 git log 中的中文正常显示