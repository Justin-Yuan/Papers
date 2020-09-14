from notion.client import NotionClient
from notion.block import PageBlock 
import itertools 


token_v2 = "0cc46833599316bda207b804ec360a187af32716ee1543edae7abe9848bb585ba60103f36571d1c8f5581fd45b98d1f3321705b7d495ee6399125c3af630c582866a5a2d96bddd9b1282976e2a02"

notion_page = "https://www.notion.so/justiny/RL-Safe-RL-5251a2a82b9542848806c00013f413f8"




"""
my_block.refresh() to update 
"""



def main():

    # Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
    client = NotionClient(token_v2=token_v2)

    # Replace this URL with the URL of the page you want to edit
    page = client.get_block(notion_page)
    import pdb; pdb.set_trace()

    print("The old title is:", page.title)

    # # Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
    # page.title = "The title has now changed, and has *live-updated* in the browser!" 


def main2():
    client = NotionClient(token_v2=token_v2)
    space = client.current_space
    store = client._store
    user_id = client.current_user.id

    # Fetch all pages, collections and space root
    all_pages = [space] + [
        client.get_block(page_id) for page_id in store._values['space'][client.current_space.id]['pages']]

    blocks = list(all_pages)
    while blocks:
        page_ids = set((page.id for page in all_pages))
        children_page_iter = itertools.chain.from_iterable(
            (block.children for block in blocks if hasattr(block, 'children')))
        children = [
            page for page in children_page_iter
            if page.id not in page_ids and page.type in (
                'page', 'collection',
            )
        ]
        all_pages.extend(children)
        blocks = children
        print('Collected %s blocks, current children %s' % (len(all_pages), len(children)))

    print('Total %s blocks' % len(all_pages))

    paper_page = None
    for p in all_pages[1:]:
        if p.title == "Papers":
            paper_page = p 


    import pdb; pdb.set_trace()

    for page in all_pages:
        permissions = page.get('permissions')
        if not permissions:
            continue
        permissions = [p for p in permissions if p.get('user_id') != user_id]
        if permissions:
            print('%s %s:' % (page.type, page.title))
            for permission in permissions:
                print('  > %s' % permission)








if __name__ == "__main__":
    # main() 
    main2()