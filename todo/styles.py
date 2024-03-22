# tailwind css styles
primary_color = "green"
secondary_color = "orange"
styles = {
    "primary_color": primary_color,
    "secondary_color": secondary_color,
    "button_primary": f"rounded bg-{primary_color}-600 px-2 py-1 text-xs font-semibold text-white shadow-sm hover:bg-{primary_color}-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-{primary_color}-600",
    
    "button_secondary": f"rounded bg-{secondary_color}-600 px-2 py-1 text-xs font-semibold text-white shadow-sm hover:bg-{primary_color}-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-{secondary_color}-600",
   
    'surface': f'border-solid border border-{primary_color}-600 rounded-lg shadow-md bg-white pl-4 pr-4 pt-2',

    'surface2': f'border-solid border border-{primary_color}-100 rounded-lg shadow-md bg-white pl-4 pr-4 pt-2 pb-2',

    'h1': "text-2xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight",
    'h2': "text-xl font-bold leading-7 text-gray-800 sm:truncate sm:text-2xl sm:tracking-tight"

}

def styles_context(request):
    return {
        "styles": styles,
    }