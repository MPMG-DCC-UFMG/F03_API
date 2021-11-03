from src.modules.items.item import ItemModel

def get_params_values(params):

    filters = []

    if params.description:
        filters.append(ItemModel.original_dsc.in_(params.description))
    if params.group:
        filters.append(ItemModel.grupo.in_(group))
    if params.units_of_measure:
        filters.append(ItemModel.dsc_unidade_medida.in_(params.units_of_measure))
    if params.city:
        filters.append(ItemModel.municipio.__eq__(params.city))
    if params.before:
        filters.append(ItemModel.data <= params.before)
    if params.after:
        filters.append(ItemModel.data >= params.after)
    if params.first_token:
        filters.append(ItemModel.primeiro_termo.__eq__(params.first_token))

    return filters
