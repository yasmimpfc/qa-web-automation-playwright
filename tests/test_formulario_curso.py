from playwright.sync_api import sync_playwright, expect


def test_usuario_solicita_informacoes_do_curso():

    with sync_playwright() as pw:

        navegador = pw.chromium.launch(headless=False)
        contexto = navegador.new_context()

        pagina = contexto.new_page()

        pagina.goto("https://hashtagtreinamentos.com")

        print(pagina.title())

        botao = (
            pagina
            .locator("div")
            .filter(has_text="Torne-se uma referência no")
            .get_by_role("link", name="Quero aprender")
        )

        with contexto.expect_page() as pagina2_info:
            botao.click()

        pagina2 = pagina2_info.value

        pagina2.goto("https://www.hashtagtreinamentos.com/curso-python")

        print(pagina2.url)
        print(pagina2.title())

        pagina2.get_by_role(
            "textbox",
            name="Seu primeiro nome"
        ).fill("Usuário Teste")

        pagina2.get_by_role(
            "textbox",
            name="Seu melhor e-mail"
        ).fill("usuarioteste@gmail.com")

        pagina2.get_by_role(
            "textbox",
            name="Seu WhatsApp com DDD"
        ).fill("+5581981112331")

        pagina2.get_by_role(
            "button",
            name="Quero acessar as informações"
        ).click()

        novo_botao = pagina2.get_by_role(
            "link",
            name="quero garantir uma vaga"
        )

        expect(novo_botao).to_be_visible()

        novo_botao.click()


    