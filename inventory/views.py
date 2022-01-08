from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import InventoryMakerForm, InventoryEditForm
from .models import Inventory
from django.shortcuts import render
from django.urls import reverse
import csv
from django.http import HttpResponse


# Create CSV
def csv_create(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    inventory_data = Inventory.objects.all()
    writer.writerow(["id", "Name", "Description"])
    for q in inventory_data:
        writer.writerow([q.id, q.name, q.description])
    return response


# Create your views here.
def inventory_create(request):
    if request.method == "POST":
        form = InventoryMakerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["inventory_name"]
            description = form.cleaned_data["inventory_description"]
            q = Inventory(name=name, description=description)
            q.save()
            return HttpResponseRedirect(reverse("inventory:inventorylist"))
        else:
            raise Http404("Invalid input")
    else:
        form = InventoryMakerForm()
    context = {"form": form}
    return render(request, "inventory/inventorycreate.html", context)


# Create your views here.
def inventory_edit(request, pk):
    q = get_object_or_404(Inventory, pk=pk)
    original_name = q.name
    if request.method == "POST":
        form = InventoryEditForm(request.POST)
        if form.is_valid():
            name_ = form.cleaned_data["inventory_name"]
            description_ = form.cleaned_data["inventory_description"]
            if original_name != name_ and Inventory.objects.filter(name=name_):
                raise Http404(
                    "Invalid input (Name probably already exists or exceeds 30 characrters)"
                )
            else:
                q.name = name_
                q.description = description_
                q.save()
                return HttpResponseRedirect(reverse("inventory:inventorylist"))
        else:
            raise Http404(
                "Invalid input (Name probably already exists or exceeds 30 characrters)"
            )
    else:
        form = InventoryMakerForm(
            initial={"inventory_name": q.name, "inventory_description": q.description},
        )
    context = {"form": form}
    return render(request, "inventory/inventoryedit.html", context)


# Create your views here.
def inventory_delete(request, pk):
    q = get_object_or_404(Inventory, pk=pk)
    q.delete()
    return HttpResponseRedirect(reverse("inventory:inventorylist"))


def get_one_inventory(request, pk):
    try:
        p = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        raise Http404("Inventory does not exist")
    context = {"inventory": p}
    return render(request, "inventory/inventory.html", context)


def inventorylist(request):
    inventory = Inventory.objects.all()
    context = {"inventories": inventory}
    return render(request, "inventory/inventorylist.html", context)
