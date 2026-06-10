import os
import subprocess

def enviar_pro_github(mensagem_commit="Automação: Atualização do projeto"):
    # Busca o token que você configurou no ambiente
    token = os.environ.get("GITHUB_TOKEN")
    
    if not token:
        print("❌ Erro: O GITHUB_TOKEN não foi encontrado no ambiente.")
        return

    try:
        print("📦 Adicionando arquivos modificados...")
        subprocess.run(["git", "add", "."], check=True)
        
        print("📝 Criando o commit...")
        subprocess.run(["git", "commit", "-m", mensagem_commit], check=True)
        
        print("🚀 Enviando para o repositório remoto (GitHub)...")
        # Força o uso do token na URL de envio de forma segura
        url_remota = f"https://{token}@github.com/robson-lisboa/automacao-relatorios.git"
        subprocess.run(["git", "remote", "set-url", "origin", url_remota], check=True)
        
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("✅ Sucesso! Seu código foi atualizado e salvo no seu GitHub.")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao rodar comandos do Git: {e}")

if __name__ == "__main__":
    enviar_pro_github()