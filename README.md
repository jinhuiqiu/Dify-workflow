# Dify-workflow
## 基于Dify的Python后端春联生成项目
## 项目结构
```
Dify-workflow/
├── app.py                 # 启动服务（后端）
├── index.html             # 前端代码
├── requirements.txt       # 项目环境依赖
└── workflow.yml           # Dify工作流
```
## 界面展示
![1750041055980](https://github.com/user-attachments/assets/d9304aaf-4462-46e5-92ad-2da6618fcdb3)
## 功能介绍
- 输入一个主题，选择对联字数(五言、七言、九言、十一言)
- 生成对联后可下载对联图片(.png)
## 安装与运行
### 运行步骤
- 导入workflow.yml到Dify并发布，找到API_KEY和API_URL填入app.py中
- 安装环境依赖
```
pip install -r requirements.txt
```
- 启动服务
```
python app.py
```
- 访问
```
http://127.0.0.1:5000
```
