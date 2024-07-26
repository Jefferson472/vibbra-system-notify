# vibbra-notify-system

Sistema de Notificação de Mensagens em Python e Django

## Sobre o Projeto

Sistema de notificação de mensagens desenvolvido em Python com o Framework Django. Este projeto visa fornecer uma plataforma única para quem necessita integrar notificações em diversos canais, como Web Push, E-mail e SMS.
O público-alvo são profissionais de tecnologia que buscam uma solução centralizada para a gestão de notificações. Seja para enviar alertas, atualizações ou emails promocionais.

### Funcionalidades Principais

1. Tela de Configuração

- Permite ao usuário criar um aplicativo e definir os canais de notificação desejados (Web Push, E-mail, SMS).
- Configuração por canal (Web Push, E-mail, SMS) para personalização detalhada.

2. Tela de Setup Web Push

- Configuração de dados básicos como nome, endereço e ícone do site.
- Personalização de mensagens de permissão permitindo alterar texto da mensagem e dos botões permitir/negar.
- Configuração da notificação de boas vindas, permitindo a personalizando dos textos, títulos e links.

3. Tela de Setup E-mail

- Configuração de dados técnicos do servidor SMTP (nome, porta, login, senha).
- Definição de dados de envio (nome e e-mail do remetente).
- Submissão de templates de e-mail em formato HTML.

4. Tela de Setup SMS

- Configuração de provedor de SMS integrado (provedor, login, senha).

5. Tela de Histórico de Notificações

- Exibição do resumo das últimas notificações enviadas com filtros específicos (data, canal, origem).
- Possibilidade de exportar os dados para PDF e Excel.
- Visualização detalhada das informações de cada notificação contendo as informações: canal de envio, data e hora de envio e recebimento, confirmação de leitura, conteúdo da notificação (título, mensagem, link de direcionamento, conteúdo do e-mail).

6. Tela de Envio Manual de Notificações

- Interface para envio manual de notificações via Web Push, E-mail e SMS.
    - **Web Push**: Contém a audiência e dados da mensagem (título, texto da mensagem, ícone e link destino);
    - **SMS**: Telefone dos usuários e texto da mensagem;
    - **Email**: Email dos destinatários e templates existentes;
- Preenchimento de dados da mensagem e envio após confirmação.


## TODO

#### 1. Avaliação do Escopo e Reuniões de Alinhamento (**Subtotal: 15 horas**)
- [x] **Avaliação detalhada do escopo do projeto** (10 horas)
- [x] **Reuniões de alinhamento e esclarecimento de dúvidas** (5 horas)

#### 2. Configuração Inicial do Projeto (**Subtotal: 6 horas**)
- [x] **Configurar ambiente de desenvolvimento** (**Subtotal: 1 horas**)
  - [x] **Instalar Python e Django**
  - [x] **Configurar o Poetry para gerenciar dependências**
  - [x] **Configurar banco de dados (Postgres)**

- [x] **Criar estrutura básica do projeto Django** (**Subtotal: 2 horas**)
  - [x] **Criar novo projeto Django**
  - [x] **Configurar settings do projeto**
  - [x] **Criar aplicação principal do projeto**

- [x] **Implementar sistema de login e senha** (**Subtotal: 3 horas**)
  - [x] **Configurar autenticação padrão do Django**
  - [x] **Criar modelo de usuário personalizado**
  - [x] **Implementar views e templates de login e registro**
  - [x] **Implementar recuperação de senha**
  - [x] **Testes de funcionalidade de login e senha**

#### 3. Telas de Configuração (**Subtotal: 8 horas**)
- [ ] **Criar interface de usuário para configuração** (2 horas)
- [ ] **Implementar lógica para criação de aplicativos** (2 horas)
- [ ] **Configuração de canais (Web Push, E-mail, SMS)** (2 horas)
- [ ] **Validação e testes** (1 horas)

#### 4. Telas de Setup Web Push (**Subtotal: 9 horas**)
- [ ] **Desenvolver interface de usuário para setup de Web Push** (1 horas)
- [ ] **Configuração de dados básicos (nome, endereço, ícone)** (2 horas)
- [ ] **Implementar lógica para personalização de mensagens de permissão** (3 horas)
- [ ] **Implementar lógica para personalização de notificações de boas-vindas** (2 horas)
- [ ] **Validação e testes** (1 horas)

#### 5. Tela de Setup E-mail (**Subtotal: 10 horas**)
- [ ] **Desenvolver interface de usuário para setup de E-mail** (1 horas)
- [ ] **Configuração de dados técnicos do servidor SMTP** (2 horas)
- [ ] **Implementar lógica para dados de envio (nome e e-mail do remetente)** (2 horas)
- [ ] **Implementar submissão de templates de e-mail (upload e armazenamento)** (4 horas)
- [ ] **Validação e testes** (1 horas)

#### 6. Tela de Setup SMS (**Subtotal: 10 horas**)
- [ ] **Desenvolver interface de usuário para setup de SMS** (4 horas)
- [ ] **Configuração de provedor de SMS integrado (login, senha)** (4 horas)
- [ ] **Validação e testes** (2 horas)

#### 7. Tela de Histórico de Notificações (**Subtotal: 10 horas**)
- [ ] **Desenvolver interface de usuário para histórico de notificações** (1 horas)
- [ ] **Implementar filtros de busca (data, canal, origem)** (2 horas)
- [ ] **Implementar exportação de dados para PDF e Excel** (4 horas)
- [ ] **Implementar visualização detalhada de notificações** (2 horas)
- [ ] **Validação e testes** (1 horas)

#### 8. Tela de Envio Manual de Notificações (**Subtotal: 16 horas**)
- [ ] **Desenvolver interface de usuário para envio manual (Web Push, E-mail, SMS)** (2 horas)
- [ ] **Implementar lógica de envio de Web Push** (6 horas)
- [ ] **Implementar lógica de envio de E-mail** (1 horas)
- [ ] **Implementar lógica de envio de SMS** (6 horas)
- [ ] **Validação e testes** (1 horas)

#### 9. Deploy (**Subtotal: 10 horas**)
- [ ] **Configuração do ambiente de produção** (**Subtotal: 3 horas**)
  - [ ] **Configurar servidor Render** (2 horas)
  - [ ] **Configurar banco de dados de produção** (1 horas)

- [ ] **Configurar CI/CD** (**Subtotal: 7 horas**)
  - [ ] **Configurar pipeline de CI/CD (GitLab CI)** (4 horas)
  - [ ] **Testar e validar a pipeline de CI/CD** (3 horas)

### Total Geral
**Estimativa total: 94 horas**


## Estimativa em DIAS do prazo de entrega:
**Estimativa total: 30 dias**

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://git.vibbra.com.br/Miranda/notify-system.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://git.vibbra.com.br/Miranda/notify-system/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!).  Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
