## ⚠️ Disclaimer

Este código é fornecido exclusivamente para fins educacionais.
O autor não se responsabiliza por qualquer uso indevido.
---

# 🛡️ Reverse Shell em Python (Projeto Educacional de Cibersegurança)

## 📌 Descrição

Este projeto foi desenvolvido com fins estritamente educacionais, com o objetivo de demonstrar como funcionam técnicas comuns utilizadas em ataques do tipo reverse shell.

O código ilustra conceitos importantes de cibersegurança, como:

* Comunicação cliente-servidor via sockets
* Execução remota de comandos
* Persistência em sistemas (autorun)
* Uso de threads para execução concorrente

⚠️ Aviso importante:
Este projeto deve ser utilizado apenas em ambientes controlados, como laboratórios, máquinas virtuais ou redes de teste. O uso indevido pode ser ilegal.

---

## 🎯 Objetivos de Aprendizado

* Entender o funcionamento básico de uma reverse shell
* Estudar técnicas de persistência em sistemas Windows
* Analisar riscos de execução remota de comandos
* Desenvolver estratégias de detecção e mitigação

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Bibliotecas padrão:

  * socket
  * subprocess
  * threading
  * os
  * sys
  * shutil

---

## 🧠 Conceitos Abordados

### 🔌 Reverse Connection (C2)

O cliente inicia uma conexão com um servidor remoto (Command & Control), permitindo controle remoto.

### 🖥️ Execução de Comandos

Comandos recebidos via socket são executados no sistema operacional.

### 🔁 Persistência (Autorun)

O script tenta se copiar para a pasta de inicialização do Windows.

### ⚡ Multithreading

Execução paralela de comandos para melhorar responsividade.

---

## 🔒 Considerações de Segurança

Este projeto demonstra comportamentos que podem ser identificados por ferramentas de segurança:

* Antivírus e EDR podem detectar execução suspeita
* Conexões de saída incomuns podem ser monitoradas
* Persistência em startup é um indicador clássico de comprometimento

---

## 🛡️ Como se Proteger

Algumas medidas defensivas contra esse tipo de técnica:

* Monitorar conexões de saída
* Restringir execução de scripts desconhecidos
* Utilizar antivírus/EDR atualizados
* Analisar alterações em diretórios de inicialização
* Aplicar princípio do menor privilégio

---

## 🧪 Ambiente de Teste Recomendado

* Máquina virtual (VirtualBox / VMware)
* Rede isolada
* Sistema operacional de teste (ex: Windows VM + Kali Linux)

---

## 📚 Uso Acadêmico

Este projeto pode ser utilizado em disciplinas como:

* Segurança da Informação
* Redes de Computadores
* Sistemas Operacionais

---

## 👨‍💻 Autor

Caio César Silva dos Santos



