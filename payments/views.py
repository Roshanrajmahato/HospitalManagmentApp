from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import DischargeSummary
from .forms import DischargeSummaryForm


# ==========================================
# 1️⃣ CREATE DISCHARGE
# ==========================================
@login_required(login_url='login')
def create_discharge(request):

    if request.method == "POST":

        form = DischargeSummaryForm(request.POST)

        if form.is_valid():

            discharge = form.save()

            print("✅ SAVED:", discharge.id)

            return redirect(
                'discharge_bill',
                pk=discharge.pk
            )

        else:

            print("❌ FORM ERRORS:", form.errors)

    else:

        form = DischargeSummaryForm()

    return render(
        request,
        "payment/create_discharge.html",
        {'form': form}
    )

# ==========================================
# 2️⃣ BILL DISPLAY VIEW
# ==========================================

@login_required(login_url='login')
def discharge_bill(request, pk):

    bill = get_object_or_404(

        DischargeSummary,
        pk=pk

    )

    return render(

        request,
        "payment/discharge_bill.html",
        {'bill': bill}

    )


# ==========================================
# 3️⃣ BILL LIST VIEW
# ==========================================

@login_required(login_url='login')
def discharge_list(request):

    bills = DischargeSummary.objects.all().order_by('-created_at')

    return render(

        request,
        "payment/discharge_list.html",
        {'bills': bills}

    )