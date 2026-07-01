from playwright.sync_api import sync_playwright, expect
import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()
    #abrir navegador
    pagina = contexto.new_page()
    #navegar para uma pagina 
    pagina.goto("https://hashtagtreinamentos.com")
    #pegar infos da pagina 
    print(pagina.title())

    #selecionar um elemento na tela
    #primeira forma xpath (não recomendado)
    #pagina.locator(xpath)
    #segunda forma, mais recomendada 
    botao = pagina.locator("div").filter(has_text="Torne-se uma referência no").get_by_role("link", name="Quero aprender")
    with contexto.expect_page() as pagina2_info:
       botao.click()

    pagina2 = pagina2_info.value   

    pagina2.goto("https://www.hashtagtreinamentos.com/curso-python")

    #selecionar varios elementos
    #divisorias = pagina.locator("div").all()

    #preencher formulário 
    pagina2.get_by_role("textbox", name="Seu primeiro nome").fill("Yasmim")
    pagina2.get_by_role("textbox", name="Seu melhor e-mail").fill("yasmimpfc@gmail.com")
    pagina2.get_by_role("textbox", name="Seu WhatsApp com DDD").fill("81981512331")
    pagina2.get_by_role("button", name="Quero acessar as informações").click()

    novo_botao = pagina2.get_by_role("link", name = "quero garantir uma vaga")
    expect(novo_botao).to_be_visible
    novo_botao.click()


    


    time.sleep(4)
    navegador.close()