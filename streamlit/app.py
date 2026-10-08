import streamlit as str

str.set_page_config(page_title="Super Calculadora de Compras", page_icon="🛒", layout="centered")

str.title("🏪 Minha Calculadora de Supermercado")
str.caption("Selecione os produtos, veja o total da compra e calcule o seu troco em tempo real.")

precos_itens = {
    "Arroz (5kg)": 25.90,
    "Feijão (1kg)": 8.50,
    "Óleo de Soja (900ml)": 6.80,
    "Açúcar (1kg)": 4.50,
    "Café Moído (500g)": 14.90,
    "Leite Integral (1L)": 5.20,
    "Pão de Forma": 7.49,
    "Manteiga (200g)": 9.80,
    "Ovos (Dúzia)": 11.00,
    "Macarrão (500g)": 3.99
}

def calcular_preco_total(itens_selecionados):
    total = sum(precos_itens[item] for item in itens_selecionados)
    return total


itens_selecionados = str.multiselect(
    label="Selecione os itens do supermercado:",
    options=list(precos_itens.keys())
)

if itens_selecionados:
    str.subheader("📋 Itens Selecionados:")
    for item in itens_selecionados:
        str.write(f"- {item}: R$ {precos_itens[item]:.2f}")
   

    total_compra = calcular_preco_total(itens_selecionados)
   
    str.divider()
    str.metric(label="Total da Compra", value=f"R$ {total_compra:.2f}")

    str.subheader(" Calculadora de Troco")

    valor_pago = str.number_input(
        label="Digite o valor pago em dinheiro (R$):", 
        min_value=0.0, 
        step=1.0, 
        format="%.2f"
    )
    
    if valor_pago > 0:
        if valor_pago >= total_compra:
            troco = valor_pago - total_compra
            str.success(f" Seu troco é de: **R$ {troco:.2f}**")
            str.balloons()  
        else:
            falta = total_compra - valor_pago
            str.error(f" O valor pago é insuficiente. Ainda faltam **R$ {falta:.2f}**.")

else:
    str.info("Nenhum item selecionado. Marque os produtos acima para ver o valor total.")
