import flet as ft
from db import main_db


def main(page: ft.Page):
    page.title = 'Products list'
    page.theme_mode = ft.ThemeMode.LIGHT
    product_list = ft.Column(spacing=30)
    main_db.init_db()
    filter_type = 'all'
    len_com_products = ft.TextField(value=main_db.get_len_products(),read_only=True)
    

    def load_products():
        product_list.controls.clear()

        len_com_products.value = f'Количество купленных вещей:{main_db.get_len_products()}'

        for product_id, product, completed in main_db.get_products(filter_type=filter_type):
            product_list.controls.append(create_product_row(product_id=product_id,product=product,completed=completed))
        page.update()

    def create_product_row(product_id, product, completed):
        product_field = ft.TextField(value=product, read_only=True, expand=True)

        checkbox = ft.Checkbox(value=bool(completed), on_change=lambda e: toggle_product(product_id, e.control.value))

        def enable_edit(_):
            product_field.read_only = False
            product_field.update()

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        def save_product(_):
            main_db.update_products(product_id=product_id, new_product=product_field.value)
            product_field.read_only = True
            product_field.update()
            page.update()

        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_product)

        def del_product(_):
            main_db.delete_products(product_id)
            load_products()
            page.update()

        del_button = ft.IconButton(icon=ft.Icons.DELETE,on_click=del_product)

        return ft.Row([checkbox, product_field, edit_button, save_button,del_button])
    
    def toggle_product(product_id, is_completed):
        main_db.update_products(product_id=product_id, completed=int(is_completed))
        load_products()

    def add_product(_):
        if product_name.value:
            product = product_name.value
            product_id = main_db.add_product(product=product)
            product_list.controls.append(create_product_row(product_id=product_id, product=product, completed=None))
            product_name.value = None
            page.update()

    product_name = ft.TextField(label='Введите название продукта', on_submit=add_product, expand=True)
    product_name_button = ft.IconButton(icon=ft.Icons.SEND,on_click=add_product)

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_products()

    def del_com_product(_):
        main_db.del_completed_product()
        load_products()
        page.update()
        
    
    
    filter_buttons = ft.Row([
        ft.ElevatedButton('Весь список продуктов', on_click=lambda e: set_filter('all'), icon=ft.Icons.ALL_INBOX, icon_color=ft.Colors.YELLOW),
        ft.ElevatedButton('Не купленные продукты', on_click=lambda e: set_filter('uncompleted'), icon=ft.Icons.WATCH_LATER, icon_color=ft.Colors.RED),
        ft.ElevatedButton("Купленные продукты", on_click=lambda e: set_filter('completed'), icon=ft.Icons.CHECK_BOX, icon_color=ft.Colors.GREEN),
        ft.ElevatedButton('Удалить список купленных продуктов',on_click=del_com_product,icon=ft.Icons.DELETE_FOREVER,icon_color=ft.Colors.RED),
        
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    

    page.add(ft.Row([product_name, product_name_button]), len_com_products,filter_buttons, product_list)
    load_products()

if __name__ == '__main__':
    main_db.init_db
    ft.app(target=main)