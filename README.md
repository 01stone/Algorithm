# Algorithm
  
<h3>vscode에서 python파일 실행 방법</h3>
  
1. Extention 설치메뉴에서 Python ```install```
2. 지정한 폴더 내에서 ```print('HelloWorld')``` 등 한 줄 코드 작성
3. ```Ctrl``` + ```Shift``` + ```B``` : 실행 단축키
4. 만약 ```No build task to run found. Configure Build Task...```이런 문구가 나온다면...
5. ```Ctrl``` + ```Shift``` + ```P```
6. ```Tasks:Configure Task```, 템플릿에서 task.json파일 만들기
7. ```Others``` : ```task.json``` 생성
8. 아래 내용으로 변경 후, 다시 실행하면 ✔
    ``` 
    {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "python execute",
                "type": "shell",
                "command": "python",  # 터미널에서 입력될 커맨드
                "options": {
                    "cwd": "${fileDirname}"
                },
                "args": [
                    "${file}"
                ],                    # 커맨드와 함께 입력되는 인자
                "group":{
                    "kind": "build",
                    "isDefault": true
                },
                "presentation": {
                    "echo": true,
                    "reveal": "always",
                    "focus": false,
                    "panel": "shared",
                    "showReuseMessage": true,
                    "clear": true
                }
            },

            {
                "label": "c execute",
                "type": "shell",
                "command": "./${fileBasenameNoExtension}",
                "group":{
                    "kind": "test",
                    "isDefault": true
                },
                "presentation": {
                    "echo": true,
                    "reveal": "always",
                    "focus": false,
                    "panel": "shared",
                    "showReuseMessage": true,
                    "clear": true
                }
            }
        ]
    }
    ```  
    
- 220104 git clone
  - git clone ```[주소]```     

- 220112 git clone & pull 시도
  - git clone ```[주소]```
  - git remote -v : 원격저장소 연결
  - git pull  
