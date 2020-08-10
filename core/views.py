from django.shortcuts import render
from django.http import HttpResponse
import json, requests
from django.http import JsonResponse




# Create your views here.
def homepage(request):
    htmlDropdown="<option>Select Amount First</option>"
    final_result=''
    url = "http://savings.gov.pk/latest/results.php"

    if request.POST.get('action') == 'post':
        if request.POST.get('forum') == 'DropDown':
            prize = request.POST.get('prize')
            if prize == "1":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="283">15 May, 2020 </option><option value="274">17 February, 2020 </option><option value="264">15 November, 2019 </option><option value="259">16 September, 2019 </option><option value="255">16 August, 2019 </option><option value="246">15 May, 2019 </option><option value="236">15 February, 2019 </option><option value="227">15 November, 2018 </option><option value="218">15 August, 2018 </option><option value="209">15 May, 2018 </option><option value="200">15 February, 2018 </option><option value="191">15 November, 2017 </option><option value="179">15 August, 2017 </option><option value="163">15 May, 2017 </option><option value="59">15 February, 2017 </option><option value="1">15 November, 2016 </option><option value="2">15 August, 2016 </option><option value="8">16 May, 2016 </option><option value="9">15 February, 2016 </option><option value="10">16 November, 2015 </option><option value="11">17 August, 2015 </option><option value="12">15 May, 2015 </option><option value="13">16 February, 2015 </option><option value="14">17 November, 2014 </option><option value="15">15 August, 2014 </option><option value="16">15 May, 2014 </option><option value="17">17 February, 2014 </option><option value="18">18 November, 2013 </option><option value="19">15 August, 2013 </option><option value="20">15 May, 2013 </option><option value="21">15 February, 2013 </option>'
            if prize == "2":
                htmlDropdown = '><option value="">Select Draw Date</option><option value="all">All</option><option value="285">15 June, 2020 </option><option value="277">16 March, 2020 </option><option value="269">16 December, 2019 </option><option value="258">16 September, 2019 </option><option value="249">17 June, 2019 </option><option value="240">15 March, 2019 </option><option value="231">17 December, 2018 </option><option value="222">17 September, 2018 </option><option value="213">19 June, 2018 </option><option value="204">15 March, 2018 </option><option value="195">15 December, 2017 </option><option value="186">15 September, 2017 </option><option value="173">15 June, 2017 </option><option value="58">15 March, 2017 </option><option value="30">15 December, 2016 </option><option value="31">15 September, 2016 </option><option value="32">15 June, 2016 </option><option value="33">15 March, 2016 </option><option value="83">15 December, 2015 </option><option value="35">15 September, 2015 </option><option value="98">15 July, 2015 </option><option value="36">15 June, 2015 </option><option value="37">16 March, 2015 </option><option value="38">15 December, 2014 </option><option value="39">15 September, 2014 </option><option value="41">17 June, 2014 </option><option value="40">16 June, 2014 </option><option value="130">17 March, 2014 </option><option value="42">16 December, 2013 </option><option value="43">16 September, 2013 </option><option value="44">17 June, 2013 </option><option value="45">15 March, 2013 </option><option value="46">17 December, 2012 </option><option value="47">17 September, 2012 </option><option value="48">15 June, 2012 </option><option value="49">15 March, 2012 </option>'
            if prize == "3":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="287">15 July, 2020 </option><option value="279">15 April, 2020 </option><option value="271">15 January, 2020 </option><option value="261">15 October, 2019 </option><option value="251">15 July, 2019 </option><option value="242">15 April, 2019 </option><option value="233">15 January, 2019 </option><option value="224">15 October, 2018 </option><option value="215">16 July, 2018 </option><option value="206">16 April, 2018 </option><option value="197">15 January, 2018 </option><option value="188">16 October, 2017 </option><option value="175">17 July, 2017 </option><option value="128">17 April, 2017 </option><option value="51">16 January, 2017 </option><option value="53">17 October, 2016 </option><option value="52">18 July, 2016 </option><option value="77">15 April, 2016 </option><option value="92">15 January, 2016 </option><option value="88">15 October, 2015 </option><option value="96">15 July, 2015 </option><option value="103">15 April, 2015 </option><option value="109">15 January, 2015 </option><option value="115">15 October, 2014 </option><option value="121">15 July, 2014 </option><option value="127">15 April, 2014 </option><option value="135">15 January, 2014 </option><option value="141">21 October, 2013 </option><option value="147">15 July, 2013 </option><option value="153">15 April, 2013 </option><option value="159">15 January, 2013 </option><option value="169">15 October, 2012 </option>'

            if prize == "4":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="282">15 May, 2020 </option><option value="275">17 February, 2020 </option><option value="265">15 November, 2019 </option><option value="254">16 August, 2019 </option><option value="245">15 May, 2019 </option><option value="237">15 February, 2019 </option><option value="228">15 November, 2018 </option><option value="219">15 August, 2018 </option><option value="210">15 May, 2018 </option><option value="201">15 February, 2018 </option><option value="192">15 November, 2017 </option><option value="178">15 August, 2017 </option><option value="164">15 May, 2017 </option><option value="50">15 February, 2017 </option><option value="54">15 November, 2016 </option><option value="57">15 August, 2016 </option><option value="56">16 May, 2016 </option><option value="80">15 February, 2016 </option><option value="85">15 November, 2015 </option><option value="91">17 August, 2015 </option><option value="100">15 May, 2015 </option><option value="106">16 February, 2015 </option><option value="112">17 November, 2014 </option><option value="118">15 August, 2014 </option><option value="124">15 May, 2014 </option><option value="132">17 February, 2014 </option><option value="138">18 November, 2013 </option><option value="144">15 August, 2013 </option><option value="150">15 May, 2013 </option><option value="156">15 February, 2013 </option><option value="166">15 November, 2012 </option><option value="181">15 August, 2012 </option>'

            if prize == "5":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="288">03 August, 2020 </option><option value="281">04 May, 2020 </option><option value="273">03 February, 2020 </option><option value="262">01 November, 2019 </option><option value="253">01 August, 2019 </option><option value="243">02 May, 2019 </option><option value="234">01 February, 2019 </option><option value="225">01 November, 2018 </option><option value="216">01 August, 2018 </option><option value="207">02 May, 2018 </option><option value="199">01 February, 2018 </option><option value="189">01 November, 2017 </option><option value="176">01 August, 2017 </option><option value="162">02 May, 2017 </option><option value="64">01 February, 2017 </option><option value="67">01 November, 2016 </option><option value="70">01 August, 2016 </option><option value="75">02 May, 2016 </option><option value="82">01 February, 2016 </option><option value="87">02 November, 2015 </option><option value="95">03 August, 2015 </option><option value="102">04 May, 2015 </option><option value="108">02 February, 2015 </option><option value="113">05 November, 2014 </option><option value="119">04 August, 2014 </option><option value="126">02 May, 2014 </option><option value="134">03 February, 2014 </option><option value="140">01 November, 2013 </option><option value="145">01 August, 2013 </option><option value="151">02 May, 2013 </option><option value="158">01 February, 2013 </option><option value="168">01 November, 2012 </option><option value="183">01 August, 2012 </option>'

            if prize == "6":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="286">02 July, 2020 </option><option value="278">01 April, 2020 </option><option value="270">02 January, 2020 </option><option value="260">01 October, 2019 </option><option value="250">02 July, 2019 </option><option value="241">01 April, 2019 </option><option value="232">02 January, 2019 </option><option value="223">01 October, 2018 </option><option value="214">03 July, 2018 </option><option value="205">02 April, 2018 </option><option value="196">02 January, 2018 </option><option value="187">02 October, 2017 </option><option value="174">04 July, 2017 </option><option value="60">03 April, 2017 </option><option value="65">03 January, 2017 </option><option value="68">03 October, 2016 </option><option value="72">04 July, 2016 </option><option value="78">01 April, 2016 </option><option value="93">04 January, 2016 </option><option value="89">01 October, 2015 </option><option value="97">02 July, 2015 </option><option value="104">01 April, 2015 </option><option value="110">02 January, 2015 </option><option value="116">01 October, 2014 </option><option value="122">02 July, 2014 </option><option value="129">01 April, 2014 </option><option value="136">02 January, 2014 </option><option value="142">01 October, 2013 </option><option value="148">02 July, 2013 </option><option value="154">01 April, 2013 </option><option value="160">02 January, 2013 </option><option value="170">01 October, 2012 </option>'

            if prize == "7":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="289">03 August, 2020 </option><option value="280">04 May, 2020 </option><option value="272">03 February, 2020 </option><option value="263">01 November, 2019 </option><option value="252">01 August, 2019 </option><option value="244">02 May, 2019 </option><option value="235">01 February, 2019 </option><option value="226">01 November, 2018 </option><option value="217">01 August, 2018 </option><option value="208">02 May, 2018 </option><option value="198">01 February, 2018 </option><option value="190">01 November, 2017 </option><option value="177">01 August, 2017 </option><option value="161">02 May, 2017 </option><option value="63">01 February, 2017 </option><option value="61">01 November, 2016 </option><option value="71">01 August, 2016 </option><option value="76">02 May, 2016 </option><option value="81">01 February, 2016 </option><option value="86">02 November, 2015 </option><option value="94">03 August, 2015 </option><option value="101">04 May, 2015 </option><option value="107">02 February, 2015 </option><option value="114">05 November, 2014 </option><option value="120">04 August, 2014 </option><option value="125">02 May, 2014 </option><option value="133">03 February, 2014 </option><option value="139">01 November, 2013 </option><option value="146">01 August, 2013 </option><option value="152">02 May, 2013 </option><option value="157">01 February, 2013 </option><option value="167">01 November, 2012 </option><option value="182">01 August, 2012 </option>'

            if prize == "8":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="247">03 June, 2019 </option><option value="238">01 March, 2019 </option><option value="229">03 December, 2018 </option><option value="220">03 September, 2018 </option><option value="211">01 June, 2018 </option><option value="202">01 March, 2018 </option><option value="193">04 December, 2017 </option><option value="184">05 September, 2017 </option><option value="171">01 June, 2017 </option><option value="62">01 March, 2017 </option><option value="84">01 December, 2016 </option><option value="66">01 December, 2016 </option><option value="69">01 September, 2016 </option><option value="74">01 June, 2016 </option><option value="79">01 March, 2016 </option><option value="90">01 September, 2015 </option><option value="99">01 June, 2015 </option><option value="105">02 March, 2015 </option><option value="111">01 December, 2014 </option><option value="117">01 September, 2014 </option><option value="123">02 June, 2014 </option><option value="131">03 March, 2014 </option><option value="137">02 December, 2013 </option><option value="143">02 September, 2013 </option><option value="149">03 June, 2013 </option><option value="155">01 March, 2013 </option><option value="165">03 December, 2012 </option><option value="180">01 September, 2012 </option>'

            if prize == "9":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="284">10 June, 2020 </option><option value="276">10 March, 2020 </option><option value="266">10 December, 2019 </option><option value="257">11 September, 2019 </option><option value="248">10 June, 2019 </option><option value="239">11 March, 2019 </option><option value="230">10 December, 2018 </option><option value="221">10 September, 2018 </option><option value="212">11 June, 2018 </option><option value="203">12 March, 2018 </option><option value="194">11 December, 2017 </option><option value="185">11 September, 2017 </option><option value="172">12 June, 2017 </option>'

            data = {'htmlDropdown': htmlDropdown}
            return HttpResponse(json.dumps(data))

        if request.POST.get('forum') == 'Result':
            country = request.POST.get('country')
            state = request.POST.get('state')
            state = state[2:2+3]
            range_from = request.POST.get('range_from')
            range_to = request.POST.get('range_to')
            pb_number_list = request.POST.get('pb_number_list')

            to_post = {
                "country": country,
                "state": state,
                "range_from": range_from,
                "range_to": range_to,
                "pb_number_list": pb_number_list,
                "btnsearch": "Search",
            }


            final_result = (requests.post(url, data = to_post)).text

            final_result = final_result[final_result.find('<div id="focus">'):]
            final_result = final_result[:final_result.find("</div></div></div>")+18]

            print(final_result)

            if len(final_result) < 25:
                final_result = '<h1 style="color: red; text-align:center;">Try Again Next Time</h1>'
            else:
                final_result = '<h1 style="color: green; text-align:center;">You Won!</h1>' + final_result


            data = {'Finalresult': final_result}

            print(data)

            return JsonResponse(data)


    context={
        "htmlDropdown": htmlDropdown,
        "Finalresult": final_result,

    }

    return render(request,'main.html',context)