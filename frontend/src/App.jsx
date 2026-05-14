import axios from "axios"
import {
  useEffect,
  useState
} from "react"



import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  BarChart,
  XAxis,
  YAxis,
  CartesianGrid,
  Bar,
  ResponsiveContainer
} from "recharts"

function App() {

  const [invoices, setInvoices] =
    useState([])

  const [analytics, setAnalytics] =
    useState(null)

  const [auditLogs, setAuditLogs] =
    useState([])

  const [selectedEmail, setSelectedEmail] =
    useState(null)

  const [loading, setLoading] =
    useState(false)

  const [uploading, setUploading] =
    useState(false)

  useEffect(() => {

    fetchInvoices()

    fetchAnalytics()

    fetchAuditLogs()

  }, [])


  const fetchInvoices = async () => {

    const response = await axios.get(
      "http://127.0.0.1:8000/invoices"
    )

    setInvoices(response.data)
  }


  const fetchAnalytics = async () => {

    const response = await axios.get(
      "http://127.0.0.1:8000/analytics"
    )

    setAnalytics(response.data)
  }


  const fetchAuditLogs = async () => {

    const response = await axios.get(
      "http://127.0.0.1:8000/audit-logs"
    )

    setAuditLogs(response.data)
  }


  const generateEmail = async (
    invoiceId
  ) => {

    setLoading(true)

    const response = await axios.get(

      `http://127.0.0.1:8000/generate-email/${invoiceId}`

    )

    setSelectedEmail(response.data)

    setLoading(false)
  }


  const sendEmail = async (
    invoiceId
  ) => {

    try {

      const response = await axios.post(

        `http://127.0.0.1:8000/send-email/${invoiceId}`

      )

      alert(response.data.message)

      fetchInvoices()

      fetchAuditLogs()

      fetchAnalytics()

    } catch (error) {

      console.log(error)

      alert("Email sending failed")
    }
  }


  const uploadCSV = async (event) => {

    const file = event.target.files[0]

    if (!file) return

    const formData = new FormData()

    formData.append("file", file)

    try {

      setUploading(true)

      await axios.post(

        "http://127.0.0.1:8000/upload-csv",

        formData,

        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      )

      alert("CSV Uploaded Successfully")

      fetchInvoices()

      fetchAnalytics()

    } catch (error) {

      console.log(error)

      alert("Upload Failed")

    } finally {

      setUploading(false)
    }
  }


  const chartData = analytics ? [

    {
      name: "Sent",
      value: analytics.sent_invoices
    },

    {
      name: "Pending",
      value: analytics.pending_invoices
    },

    {
      name: "Escalated",
      value: analytics.escalated
    }

  ] : []


  return (

    <div className="min-h-screen bg-gray-100 flex">

      {/* Sidebar */}

      <div className="w-64 bg-gray-900 text-white p-6">

        <h1 className="text-2xl font-bold mb-10">
          Finance Agent
        </h1>

        <div className="space-y-4">

          <div className="bg-gray-800 p-4 rounded-lg">
            Dashboard
          </div>

          <div className="bg-gray-800 p-4 rounded-lg">
            Audit Logs
          </div>

          <div className="bg-gray-800 p-4 rounded-lg">
            AI Emails
          </div>

        </div>

      </div>


      {/* Main Content */}

      <div className="flex-1 p-10">

        {/* Header */}

        <div className="flex justify-between items-center mb-10">

          <div>

            <h1 className="text-4xl font-bold">
              Finance Credit Dashboard
            </h1>

            <p className="text-gray-500 mt-2">
              AI-powered invoice follow-up system
            </p>

          </div>


          {/* Upload CSV */}

          <label className="bg-blue-600 text-white px-6 py-3 rounded-lg cursor-pointer hover:bg-blue-700">

            {
              uploading
              ? "Uploading..."
              : "Upload CSV"
            }

            <input
              type="file"
              accept=".csv"
              className="hidden"
              onChange={uploadCSV}
            />

          </label>

        </div>


        {/* Analytics Cards */}

        {analytics && (

          <div className="grid grid-cols-4 gap-6 mb-10">

            <div className="bg-white p-6 rounded-xl shadow-lg">

              <p className="text-gray-500">
                Total Invoices
              </p>

              <h2 className="text-4xl font-bold mt-2">
                {analytics.total_invoices}
              </h2>

            </div>


            <div className="bg-white p-6 rounded-xl shadow-lg">

              <p className="text-gray-500">
                Sent
              </p>

              <h2 className="text-4xl font-bold text-green-600 mt-2">
                {analytics.sent_invoices}
              </h2>

            </div>


            <div className="bg-white p-6 rounded-xl shadow-lg">

              <p className="text-gray-500">
                Pending
              </p>

              <h2 className="text-4xl font-bold text-yellow-600 mt-2">
                {analytics.pending_invoices}
              </h2>

            </div>


            <div className="bg-white p-6 rounded-xl shadow-lg">

              <p className="text-gray-500">
                Escalated
              </p>

              <h2 className="text-4xl font-bold text-red-600 mt-2">
                {analytics.escalated}
              </h2>

            </div>

          </div>
        )}


        {/* Charts */}

        <div className="grid grid-cols-2 gap-8 mb-10">

          <div className="bg-white p-6 rounded-xl shadow-lg h-[350px]">

            <h2 className="text-2xl font-bold mb-6">
              Invoice Status Distribution
            </h2>

            <ResponsiveContainer width="100%" height="100%">

              <PieChart>

                <Pie
                  data={chartData}
                  dataKey="value"
                  nameKey="name"
                  outerRadius={100}
                  label
                >

                  <Cell fill="#22c55e" />
                  <Cell fill="#eab308" />
                  <Cell fill="#ef4444" />

                </Pie>

                <Tooltip />

              </PieChart>

            </ResponsiveContainer>

          </div>


          <div className="bg-white p-6 rounded-xl shadow-lg h-[350px]">

            <h2 className="text-2xl font-bold mb-6">
              Invoice Analytics
            </h2>

            <ResponsiveContainer width="100%" height="100%">

              <BarChart data={chartData}>

                <CartesianGrid strokeDasharray="3 3" />

                <XAxis dataKey="name" />

                <YAxis />

                <Tooltip />

                <Bar dataKey="value" fill="#2563eb" />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </div>


        {/* Invoice Table */}

        <div className="bg-white rounded-xl shadow-lg p-6 mb-10 overflow-x-auto">

          <h2 className="text-2xl font-bold mb-6">
            Invoices
          </h2>

          <table className="w-full">

            <thead>

              <tr className="bg-gray-200">

                <th className="p-4 text-left">
                  Invoice
                </th>

                <th className="p-4 text-left">
                  Client
                </th>

                <th className="p-4 text-left">
                  Amount
                </th>

                <th className="p-4 text-left">
                  Stage
                </th>

                <th className="p-4 text-left">
                  Status
                </th>

                <th className="p-4 text-left">
                  Actions
                </th>

              </tr>

            </thead>

            <tbody>

              {invoices.map((invoice) => (

                <tr
                  key={invoice.id}
                  className="border-b hover:bg-gray-50"
                >

                  <td className="p-4">
                    {invoice.invoice_no}
                  </td>

                  <td className="p-4">
                    {invoice.client_name}
                  </td>

                  <td className="p-4">
                    ₹{invoice.amount}
                  </td>

                  <td className="p-4">

                    <span className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm">

                      {invoice.followup_stage}

                    </span>

                  </td>

                  <td className="p-4">

                    <span className={

                      invoice.status === "Sent"

                      ? "bg-green-100 text-green-700 px-3 py-1 rounded-full"

                      : invoice.status === "Escalated"

                      ? "bg-red-100 text-red-700 px-3 py-1 rounded-full"

                      : "bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full"
                    }>

                      {invoice.status}

                    </span>

                  </td>

                  <td className="p-4 flex gap-3">

                    <button

                      onClick={() =>
                        generateEmail(invoice.id)
                      }

                      className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
                    >

                      Preview

                    </button>


                    <button

                      onClick={() =>
                        sendEmail(invoice.id)
                      }

                      className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700"
                    >

                      Send Email

                    </button>

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>


        {/* Email Preview */}

        {loading && (

          <div className="mb-6 text-xl font-semibold">
            Generating AI Email...
          </div>
        )}


        {selectedEmail && (

          <div className="bg-white p-8 rounded-xl shadow-lg mb-10">

            <h2 className="text-3xl font-bold mb-6">
              AI Generated Email
            </h2>

            <div className="mb-6">

              <p className="font-bold mb-2">
                Subject
              </p>

              <div className="bg-gray-100 p-4 rounded-lg">

                {
                  selectedEmail.generated_email.subject
                }

              </div>

            </div>


            <div>

              <p className="font-bold mb-2">
                Email Body
              </p>

              <div className="bg-gray-100 p-6 rounded-lg whitespace-pre-line leading-relaxed">

                {
                  selectedEmail.generated_email.body
                }

              </div>

            </div>

          </div>
        )}


        {/* Audit Logs */}

        <div className="bg-white rounded-xl shadow-lg p-6">

          <h2 className="text-2xl font-bold mb-6">
            Audit Logs
          </h2>

          <table className="w-full">

            <thead>

              <tr className="bg-gray-200">

                <th className="p-4 text-left">
                  Invoice
                </th>

                <th className="p-4 text-left">
                  Client
                </th>

                <th className="p-4 text-left">
                  Stage
                </th>

                <th className="p-4 text-left">
                  Status
                </th>

                <th className="p-4 text-left">
                  Timestamp
                </th>

              </tr>

            </thead>

            <tbody>

              {auditLogs.map((log) => (

                <tr
                  key={log.id}
                  className="border-b"
                >

                  <td className="p-4">
                    {log.invoice_no}
                  </td>

                  <td className="p-4">
                    {log.client_name}
                  </td>

                  <td className="p-4">
                    {log.stage}
                  </td>

                  <td className="p-4">

                    <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full">

                      {log.send_status}

                    </span>

                  </td>

                  <td className="p-4">
                    {log.timestamp}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

    </div>
  )
}

export default App